# WeIntern AI Internship — Minor Project
**Organization:** WeIntern Pvt Ltd

**Intern:** Vratika Kumawat

---

## Project Summary
| Detail | Description |
|--------|-------------|
| Project Title | AI-Based Plant Disease Detection |
| Type | Minor Project — Group Submission |
| Group | Group 3 — AI Interns |
| Model | MobileNetV2 (Transfer Learning) |
| Dataset | PlantVillage |
| Deployment | Hugging Face Spaces |
| Status | ✅ Complete & Live |

---

## Live Demo
**Hugging Face:** [https://huggingface.co/spaces/Vratika7/agrishield-ai](https://huggingface.co/spaces/Vratika7/agrishield-ai)

---

## Project Description
AgriShield AI is a web-based plant disease detection system that uses a pretrained MobileNetV2 CNN model to classify leaf images into 38 disease categories across multiple crops. Users can upload a leaf photo or use a live camera to get an instant diagnosis along with treatment and remedy suggestions.

---

## Features
- Upload or capture leaf images for real-time disease classification
- Supports 38 plant disease classes across 14 crops
- Displays confidence score with animated ring visualization
- Provides diagnosis, cause, prevention, organic and chemical remedy for each disease
- Sample leaf gallery for quick testing

---

## Tech Stack
- TensorFlow / Keras — MobileNetV2 model for image classification
- Flask — Python backend and REST API
- OpenCV / Pillow — image preprocessing
- HTML / CSS / JavaScript — frontend UI
- Docker — containerized deployment
- Hugging Face Spaces — cloud hosting

---

## Dataset
- **Name:** PlantVillage Dataset
- **Source:** Kaggle (PlantVillage)
- **Classes:** 38 (disease + healthy combinations)
- **Crops covered:** Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato

---

## Model Details
- **Architecture:** MobileNetV2 (pretrained on ImageNet)
- **Input Size:** 224x224 RGB
- **Preprocessing:** MobileNetV2 preprocess_input (scales pixels to [-1, 1])
- **Output:** Softmax probabilities over 38 classes
- **File:** plant_disease_model.h5

---

## Folder Structure
```
Minor-Project-Plant-Disease-Detection/
├── app.py                        # Flask backend + prediction route
├── remedies.py                   # Disease remedy lookup table (38 classes)
├── class_indices.json            # Class index to label mapping
├── plant_disease_model.h5        # Trained MobileNetV2 model
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Docker config for Hugging Face deployment
├── templates/
│   └── index.html                # Main frontend UI
└── static/
    ├── css/
    │   └── style.css             # Dark glassmorphism design system
    ├── js/
    │   └── main.js               # Frontend interactivity
    └── samples/                  # Sample leaf images for testing
```

---

## How to Run Locally
1. Clone this repository
2. Navigate to the project folder
3. Install dependencies:
   ```
   pip3 install -r requirements.txt
   ```
4. Run the Flask app:
   ```
   python3 app.py
   ```
5. Open `http://localhost:7860` in your browser

---

## Libraries Used
- TensorFlow — model loading and inference
- Flask — web framework and API routing
- Pillow — image loading and resizing
- NumPy — array operations
- OpenCV — image processing utilities

---

## Author
**Vratika Kumawat** | WeIntern AI Internship 2025 | Group 3
