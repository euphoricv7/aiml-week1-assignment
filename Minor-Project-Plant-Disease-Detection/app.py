import os
import base64
import numpy as np
import cv2
from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from PIL import Image
import json
import io
from remedies import get_remedy

app = Flask(__name__)


# ===============================
# TensorFlow Model Loading
# ===============================

MODEL_PATH = "plant_disease_model.h5"
CLASS_INDEX_PATH = "class_indices.json"

model = load_model(MODEL_PATH)
with open(CLASS_INDEX_PATH, "r") as f:
    class_indices = json.load(f)

CLASS_NAMES = list(class_indices.values())

DISPLAY_NAMES = {
    cls: cls.replace("___", " - ").replace("_", " ")
    for cls in CLASS_NAMES
}


# Reverse mapping
idx_to_class = {v: k for k, v in class_indices.items()}

print("✅ TensorFlow model loaded successfully.")



def preprocess_image(image_file):
    """
    Preprocess uploaded image for TensorFlow MobileNetV2 model
    """

    image = Image.open(image_file).convert("RGB")
    image = image.resize((224, 224))

    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array = preprocess_input(img_array)
    img_array = tf.expand_dims(img_array, axis=0)

    return img_array



@app.route('/')
def index():
    # Pass crops list for samples testing
    return render_template('index.html',  classes=CLASS_NAMES, display_names=DISPLAY_NAMES)

def cv_analyze_leaf(img):
    """
    Analyzes leaf using OpenCV color segmentation and shape metrics.
    Returns: A tuple (probs, crop, metrics) or None if no leaf found.
    """
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    size = img.shape[0]
    
    # 1. Define color threshold masks (in HSV)
    # Green leaf range
    lower_green = np.array([33, 20, 20])
    upper_green = np.array([90, 255, 255])
    # Yellow leaf range (chlorosis / yellowing)
    lower_yellow = np.array([16, 25, 30])
    upper_yellow = np.array([32, 255, 255])
    # Orange/rust range
    lower_orange = np.array([5, 45, 45])
    upper_orange = np.array([15, 255, 255])
    # Brown/decay range
    lower_brown = np.array([0, 15, 15])
    upper_brown = np.array([20, 255, 120])
    
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)
    mask_brown = cv2.inRange(hsv, lower_brown, upper_brown)
    
    # Combine masks to find leaf
    leaf_mask = cv2.bitwise_or(mask_green, mask_yellow)
    leaf_mask = cv2.bitwise_or(leaf_mask, mask_orange)
    leaf_mask = cv2.bitwise_or(leaf_mask, mask_brown)
    
    # Find contours
    contours, _ = cv2.findContours(leaf_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None
        
    c = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(c)
    if area < (img.shape[0] * img.shape[1] * 0.04): # Less than 4% of image
        return None
        
    # Isolate leaf area
    clean_leaf_mask = np.zeros_like(leaf_mask)
    cv2.drawContours(clean_leaf_mask, [c], -1, 255, -1)
    
    # 2. Shape analysis
    aspect_ratio = 1.0
    solidity = 1.0
    if len(c) >= 5:
        try:
            ellipse = cv2.fitEllipse(c)
            center, axes, angle = ellipse
            major_axis = max(axes)
            minor_axis = min(axes)
            aspect_ratio = major_axis / (minor_axis + 1e-5)
        except Exception:
            # Fallback aspect ratio using bounding box
            x, y, w, h = cv2.boundingRect(c)
            aspect_ratio = max(w, h) / (min(w, h) + 1e-5)
            
        hull = cv2.convexHull(c)
        hull_area = cv2.contourArea(hull)
        solidity = area / (hull_area + 1e-5)
        
    # Crop classification based on morphology
    if aspect_ratio > 2.5:
        detected_crop = "corn"
    elif solidity > 0.81:
        detected_crop = "potato"
    else:
        detected_crop = "tomato"
        
    # 3. Color ratio analysis inside the isolated leaf contour
    leaf_pixels = np.sum(clean_leaf_mask == 255)
    
    green_pixels = np.sum((mask_green == 255) & (clean_leaf_mask == 255))
    yellow_pixels = np.sum((mask_yellow == 255) & (clean_leaf_mask == 255))
    orange_pixels = np.sum((mask_orange == 255) & (clean_leaf_mask == 255))
    brown_pixels = np.sum((mask_brown == 255) & (clean_leaf_mask == 255))
    
    green_ratio = green_pixels / (leaf_pixels + 1e-5)
    yellow_ratio = yellow_pixels / (leaf_pixels + 1e-5)
    orange_ratio = orange_pixels / (leaf_pixels + 1e-5)
    brown_ratio = brown_pixels / (leaf_pixels + 1e-5)
    
    # Calculate scores for all 9 classes based on crop and color properties
    scores = {cls: 0.001 for cls in CLASSES} # Laplace smoothing
    
    if detected_crop == "corn":
        # Corn Rust
        scores["corn_common_rust"] = orange_ratio * 6.0
        # Corn Leaf Blight
        scores["corn_leaf_blight"] = brown_ratio * 4.0 + yellow_ratio * 1.5
        # Corn Healthy
        scores["corn_healthy"] = green_ratio * 2.0
    elif detected_crop == "potato":
        scores["potato_healthy"] = green_ratio * 2.0
        if brown_ratio > 0.12:
            scores["potato_late_blight"] = brown_ratio * 5.0 + yellow_ratio * 2.0
            scores["potato_early_blight"] = brown_ratio * 1.5
        else:
            scores["potato_early_blight"] = brown_ratio * 4.5 + yellow_ratio * 2.0
            scores["potato_late_blight"] = brown_ratio * 1.0
    elif detected_crop == "tomato":
        scores["tomato_healthy"] = green_ratio * 2.0
        if brown_ratio > 0.12:
            scores["tomato_late_blight"] = brown_ratio * 5.0 + yellow_ratio * 2.0
            scores["tomato_early_blight"] = brown_ratio * 1.5
        else:
            scores["tomato_early_blight"] = brown_ratio * 4.5 + yellow_ratio * 2.0
            scores["tomato_late_blight"] = brown_ratio * 1.0
            
    # Add cross-crop penalty to suppress incorrect crops
    for cls in scores:
        if not cls.startswith(detected_crop):
            scores[cls] *= 0.05
            
    # Normalize scores to form a probability distribution
    total_score = sum(scores.values())
    probs = np.zeros(len(CLASSES))
    for idx, cls in enumerate(CLASSES):
        probs[idx] = scores[cls] / (total_score + 1e-10)
        
    return probs, detected_crop, {
        "green": float(green_ratio),
        "yellow": float(yellow_ratio),
        "orange": float(orange_ratio),
        "brown": float(brown_ratio),
        "solidity": float(solidity),
        "aspect_ratio": float(aspect_ratio)
    }

@app.route('/predict', methods=['POST'])
def predict():

    img_data = None

    # ---------- Upload ----------
    if 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            img_data = file.read()

    # ---------- Webcam ----------
    elif 'image' in request.form:

        base64_str = request.form['image']

        if ',' in base64_str:
            base64_str = base64_str.split(',')[1]

        img_data = base64.b64decode(base64_str)

    if img_data is None:
        return jsonify({"error": "No image provided"}), 400


    # ---------- TensorFlow Preprocessing ----------
    img = preprocess_image(io.BytesIO(img_data))

    # ---------- Prediction ----------
    prediction = model.predict(img, verbose=0)

    confidence = float(np.max(prediction))

    predicted_index = int(np.argmax(prediction))

    predicted_class = class_indices[str(predicted_index)]

    display_name = predicted_class.replace("___"," - ").replace("_"," ")

    remedy = get_remedy(predicted_class)


    return jsonify({

        "class": predicted_class,

        "display_name": display_name,

        "confidence": confidence,

        "remedy": remedy

    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7860)
