"""
remedies.py
Simple lookup table mapping PlantVillage-style class names to plain-language
remedy/treatment suggestions. Class names follow the "Crop___Disease" pattern
used by the standard PlantVillage folder structure.

Extend this dictionary to match whatever class names your trained model
actually outputs (check class_indices.json after training).
"""




REMEDIES = {
"Apple___Apple_scab": {
    "diagnosis": "Apple Scab is a common fungal disease that causes olive-green to dark brown spots on leaves and fruits, reducing fruit quality and yield.",
    "cause": "Caused by the fungus Venturia inaequalis, which spreads rapidly during cool and wet spring conditions.",
    "prevention": [
        "Collect and destroy fallen infected leaves.",
        "Prune trees to improve air circulation.",
        "Avoid overhead irrigation.",
        "Use disease-resistant apple varieties whenever possible."
    ],
    "organic": [
        "Apply neem oil during early disease development.",
        "Spray compost tea to strengthen plant immunity.",
        "Use Bacillus subtilis based biofungicides."
    ],
    "chemical": [
        "Captan",
        "Myclobutanil",
        "Mancozeb (follow recommended dosage)"
    ]
},
"Apple___Black_rot": {
    "diagnosis": "Black Rot causes dark circular lesions on leaves, fruit rot, and cankers on branches, significantly affecting fruit production.",
    "cause": "Caused by the fungus Botryosphaeria obtusa, which survives in infected wood and mummified fruits.",
    "prevention": [
        "Remove infected fruits and branches.",
        "Destroy mummified fruits.",
        "Maintain orchard sanitation.",
        "Prune infected twigs regularly."
    ],
    "organic": [
        "Neem oil spray.",
        "Copper-based organic fungicide.",
        "Trichoderma biofungicide."
    ],
    "chemical": [
        "Captan",
        "Thiophanate-methyl",
        "Mancozeb"
    ]
},
"Apple___Black_rot": {
    "diagnosis": "Black Rot causes dark circular lesions on leaves, fruit rot, and cankers on branches, significantly affecting fruit production.",
    "cause": "Caused by the fungus Botryosphaeria obtusa, which survives in infected wood and mummified fruits.",
    "prevention": [
        "Remove infected fruits and branches.",
        "Destroy mummified fruits.",
        "Maintain orchard sanitation.",
        "Prune infected twigs regularly."
    ],
    "organic": [
        "Neem oil spray.",
        "Copper-based organic fungicide.",
        "Trichoderma biofungicide."
    ],
    "chemical": [
        "Captan",
        "Thiophanate-methyl",
        "Mancozeb"
    ]
},
"Apple___Cedar_apple_rust": {
    "diagnosis": "Cedar Apple Rust produces bright orange-yellow spots on leaves and may reduce fruit quality.",
    "cause": "Caused by Gymnosporangium juniperi-virginianae, which requires both cedar and apple trees to complete its life cycle.",
    "prevention": [
        "Remove nearby infected cedar hosts if possible.",
        "Plant resistant cultivars.",
        "Improve orchard ventilation.",
        "Monitor trees during spring."
    ],
    "organic": [
        "Neem oil.",
        "Sulfur-based organic fungicide.",
        "Copper fungicide."
    ],
    "chemical": [
        "Myclobutanil",
        "Propiconazole",
        "Mancozeb"
    ]
},
"Apple___healthy": {
    "diagnosis": "No disease detected. The apple plant appears healthy.",
    "cause": "Healthy foliage with no visible symptoms of disease.",
    "prevention": [
        "Continue routine monitoring.",
        "Provide balanced fertilization.",
        "Maintain regular irrigation.",
        "Prune trees annually."
    ],
    "organic": [
        "Apply compost regularly.",
        "Maintain healthy soil microbes."
    ],
    "chemical": [
        "No chemical treatment required."
    ]
},
"Blueberry___healthy": {
    "diagnosis": "No disease detected. The blueberry plant appears healthy.",
    "cause": "Leaves show no visible disease symptoms.",
    "prevention": [
        "Maintain proper irrigation.",
        "Prune annually.",
        "Monitor regularly for pests."
    ],
    "organic": [
        "Apply organic compost.",
        "Use seaweed extract occasionally."
    ],
    "chemical": [
        "No chemical treatment required."
    ]
},
"Cherry_(including_sour)___healthy": {
    "diagnosis": "No disease detected. The cherry plant is healthy.",
    "cause": "Healthy foliage without visible infection.",
    "prevention": [
        "Maintain orchard sanitation.",
        "Provide balanced nutrients.",
        "Monitor periodically."
    ],
    "organic": [
        "Organic compost.",
        "Neem oil for preventive care."
    ],
    "chemical": [
        "No chemical treatment required."
    ]
},

"Cherry_(including_sour)___Powdery_mildew": {
    "diagnosis": "Powdery Mildew appears as white powdery fungal growth on leaves and young shoots.",
    "cause": "Caused by Podosphaera species under warm days and cool nights with high humidity.",
    "prevention": [
        "Prune infected shoots.",
        "Improve air circulation.",
        "Avoid excessive nitrogen fertilizer."
    ],
    "organic": [
        "Neem oil spray.",
        "Potassium bicarbonate spray.",
        "Milk spray (preventive)."
    ],
    "chemical": [
        "Sulfur fungicide",
        "Myclobutanil",
        "Propiconazole"
    ]
},
"Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
    "diagnosis": "Gray Leaf Spot causes long rectangular gray to brown lesions that reduce photosynthesis and grain yield.",
    "cause": "Caused by the fungus Cercospora zeae-maydis, which spreads rapidly in warm and humid conditions.",
    "prevention": [
        "Practice crop rotation.",
        "Remove infected crop residues.",
        "Grow resistant corn hybrids.",
        "Avoid prolonged leaf wetness."
    ],
    "organic": [
        "Apply Trichoderma biofungicide.",
        "Use neem oil as preventive protection.",
        "Maintain healthy soil using compost."
    ],
    "chemical": [
        "Azoxystrobin",
        "Propiconazole",
        "Pyraclostrobin"
    ]
},
"Corn_(maize)___Common_rust_": {
    "diagnosis": "Common Rust produces small reddish-brown pustules on both leaf surfaces.",
    "cause": "Caused by the fungus Puccinia sorghi under cool and moist weather conditions.",
    "prevention": [
        "Use resistant hybrids.",
        "Monitor fields regularly.",
        "Avoid excessive nitrogen application.",
        "Destroy infected crop debris."
    ],
    "organic": [
        "Neem oil spray.",
        "Compost tea application.",
        "Maintain proper plant nutrition."
    ],
    "chemical": [
        "Propiconazole",
        "Azoxystrobin",
        "Tebuconazole"
    ]
},
"Corn_(maize)___healthy": {
    "diagnosis": "No disease detected. Corn plant appears healthy.",
    "cause": "Leaves are healthy without visible disease symptoms.",
    "prevention": [
        "Continue routine monitoring.",
        "Maintain balanced fertilization.",
        "Ensure proper irrigation.",
        "Control weeds regularly."
    ],
    "organic": [
        "Apply compost periodically.",
        "Use biofertilizers."
    ],
    "chemical": [
        "No chemical treatment required."
    ]
},
"Corn_(maize)___Northern_Leaf_Blight": {
    "diagnosis": "Northern Leaf Blight causes long gray-green lesions that gradually turn brown and reduce yield.",
    "cause": "Caused by Exserohilum turcicum under cool, humid weather.",
    "prevention": [
        "Practice crop rotation.",
        "Use resistant varieties.",
        "Remove infected residues.",
        "Avoid overcrowding."
    ],
    "organic": [
        "Neem oil spray.",
        "Trichoderma biofungicide.",
        "Compost tea application."
    ],
    "chemical": [
        "Mancozeb",
        "Azoxystrobin",
        "Propiconazole"
    ]
},
"Grape___Black_rot": {
    "diagnosis": "Black Rot causes circular brown lesions on leaves and shriveled black fruits.",
    "cause": "Caused by the fungus Guignardia bidwellii during warm and wet weather.",
    "prevention": [
        "Remove infected leaves and fruits.",
        "Prune vines for better airflow.",
        "Maintain vineyard sanitation.",
        "Avoid overhead irrigation."
    ],
    "organic": [
        "Neem oil spray.",
        "Copper-based fungicide.",
        "Trichoderma biofungicide."
    ],
    "chemical": [
        "Mancozeb",
        "Myclobutanil",
        "Captan"
    ]
},
"Grape___Esca_(Black_Measles)": {
    "diagnosis": "Esca causes leaf discoloration, wood decay, and reduced vine vigor.",
    "cause": "Associated with several trunk-invading fungi that infect grapevine wood.",
    "prevention": [
        "Prune during dry weather.",
        "Disinfect pruning tools.",
        "Remove infected vines.",
        "Avoid trunk injuries."
    ],
    "organic": [
        "Apply Trichoderma on pruning wounds.",
        "Improve soil health using compost."
    ],
    "chemical": [
        "No fully effective chemical cure available.",
        "Use registered wound protectants."
    ]
},
"Grape___healthy": {
    "diagnosis": "No disease detected. Grapevine appears healthy.",
    "cause": "Healthy foliage without visible disease symptoms.",
    "prevention": [
        "Maintain vineyard sanitation.",
        "Prune regularly.",
        "Monitor vines frequently.",
        "Maintain balanced irrigation."
    ],
    "organic": [
        "Organic compost.",
        "Seaweed extract."
    ],
    "chemical": [
        "No chemical treatment required."
    ]
},
"Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
    "diagnosis": "Leaf Blight causes brown angular lesions leading to premature leaf drop.",
    "cause": "Caused by Isariopsis species, especially under humid conditions.",
    "prevention": [
        "Remove infected leaves.",
        "Improve air circulation.",
        "Avoid overhead irrigation.",
        "Maintain proper vine spacing."
    ],
    "organic": [
        "Neem oil spray.",
        "Copper fungicide.",
        "Trichoderma biofungicide."
    ],
    "chemical": [
        "Copper Oxychloride",
        "Mancozeb",
        "Propiconazole"
    ]
},
"Orange___Haunglongbing_(Citrus_greening)": {
    "diagnosis": "Citrus Greening (HLB) is one of the most destructive citrus diseases, causing yellow shoots, blotchy mottled leaves, misshapen fruits, and gradual tree decline.",
    "cause": "Caused by the bacterium Candidatus Liberibacter asiaticus and transmitted by the Asian citrus psyllid.",
    "prevention": [
        "Use certified disease-free nursery plants.",
        "Control citrus psyllid populations.",
        "Inspect orchards regularly.",
        "Remove severely infected trees."
    ],
    "organic": [
        "Use neem oil to suppress psyllids.",
        "Release beneficial insects such as ladybugs.",
        "Maintain healthy soil with organic compost."
    ],
    "chemical": [
        "Imidacloprid",
        "Thiamethoxam",
        "Apply insecticides only as recommended by agricultural authorities."
    ]
},
"Peach___Bacterial_spot": {
    "diagnosis": "Bacterial Spot causes dark lesions on leaves and fruits, resulting in premature leaf drop and reduced fruit quality.",
    "cause": "Caused by Xanthomonas arboricola pv. pruni under warm and humid conditions.",
    "prevention": [
        "Use disease-free planting material.",
        "Prune infected branches.",
        "Improve air circulation.",
        "Avoid overhead irrigation."
    ],
    "organic": [
        "Copper-based organic spray.",
        "Neem oil application.",
        "Maintain orchard sanitation."
    ],
    "chemical": [
        "Copper Oxychloride",
        "Copper Hydroxide",
        "Streptomycin (where permitted)"
    ]
},
"Peach___healthy": {
    "diagnosis": "No disease detected. Peach plant appears healthy.",
    "cause": "Leaves show no visible disease symptoms.",
    "prevention": [
        "Maintain balanced irrigation.",
        "Apply fertilizers as recommended.",
        "Monitor for pests and diseases."
    ],
    "organic": [
        "Apply compost regularly.",
        "Use biofertilizers."
    ],
    "chemical": [
        "No chemical treatment required."
    ]
},
"Pepper,_bell___Bacterial_spot": {
    "diagnosis": "Bacterial Spot causes small dark lesions on leaves and fruits, reducing yield and fruit quality.",
    "cause": "Caused by Xanthomonas species that spread through infected seeds, rain splash, and contaminated tools.",
    "prevention": [
        "Use certified disease-free seeds.",
        "Avoid working in wet fields.",
        "Rotate crops.",
        "Remove infected plants."
    ],
    "organic": [
        "Neem oil spray.",
        "Copper-based organic fungicide.",
        "Improve soil microbial activity."
    ],
    "chemical": [
        "Copper Oxychloride",
        "Copper Hydroxide",
        "Mancozeb (as recommended)"
    ]
},
"Pepper,_bell___healthy": {
    "diagnosis": "No disease detected. Bell pepper plant appears healthy.",
    "cause": "Healthy leaves without visible symptoms.",
    "prevention": [
        "Maintain regular irrigation.",
        "Monitor crop regularly.",
        "Ensure balanced fertilization."
    ],
    "organic": [
        "Apply compost.",
        "Use seaweed extract."
    ],
    "chemical": [
        "No chemical treatment required."
    ]
},
"Potato___Early_blight": {
    "diagnosis": "Early Blight causes concentric brown lesions with target-like rings on older leaves, reducing photosynthesis and tuber yield.",
    "cause": "Caused by Alternaria solani, which survives in infected crop debris and spreads under warm, humid conditions.",
    "prevention": [
        "Practice crop rotation.",
        "Remove infected leaves.",
        "Avoid overhead irrigation.",
        "Maintain balanced fertilization."
    ],
    "organic": [
        "Neem oil spray.",
        "Trichoderma biofungicide.",
        "Compost tea application."
    ],
    "chemical": [
        "Chlorothalonil",
        "Mancozeb",
        "Azoxystrobin"
    ]
},
"Potato___healthy": {
    "diagnosis": "No disease detected. Potato plant appears healthy.",
    "cause": "Healthy foliage without visible infection.",
    "prevention": [
        "Monitor fields regularly.",
        "Maintain balanced irrigation.",
        "Use certified seed potatoes."
    ],
    "organic": [
        "Organic compost.",
        "Biofertilizers."
    ],
    "chemical": [
        "No chemical treatment required."
    ]
},
"Potato___Late_blight": {
    "diagnosis": "Late Blight is a rapidly spreading disease that causes dark water-soaked lesions on leaves, stems, and tubers, leading to severe crop loss.",
    "cause": "Caused by Phytophthora infestans, an oomycete (water mold) that thrives in cool and humid weather.",
    "prevention": [
        "Remove infected leaves immediately.",
        "Avoid overhead irrigation.",
        "Ensure proper spacing for airflow.",
        "Practice crop rotation.",
        "Use certified disease-free seed tubers."
    ],
    "organic": [
        "Apply neem oil every 7–10 days.",
        "Use Trichoderma-based biofungicide.",
        "Spray compost tea to improve plant resistance.",
        "Destroy infected plant debris."
    ],
    "chemical": [
        "Mancozeb",
        "Copper Oxychloride",
        "Metalaxyl + Mancozeb",
        "Apply fungicides according to agricultural recommendations."
    ]
},
"Raspberry___healthy": {
    "diagnosis": "No disease detected. Raspberry plant appears healthy.",
    "cause": "Leaves are healthy without any visible disease symptoms.",
    "prevention": [
        "Monitor plants regularly.",
        "Maintain proper irrigation.",
        "Prune weak or damaged canes.",
        "Keep the planting area clean."
    ],
    "organic": [
        "Apply organic compost.",
        "Use vermicompost periodically."
    ],
    "chemical": [
        "No chemical treatment required."
    ]
},
"Soybean___healthy": {
    "diagnosis": "No disease detected. Soybean crop appears healthy.",
    "cause": "Healthy foliage with no visible symptoms of infection.",
    "prevention": [
        "Use certified quality seeds.",
        "Maintain balanced soil fertility.",
        "Monitor fields regularly.",
        "Control weeds properly."
    ],
    "organic": [
        "Apply biofertilizers.",
        "Use compost to improve soil fertility."
    ],
    "chemical": [
        "No chemical treatment required."
    ]
},
"Squash___Powdery_mildew": {
    "diagnosis": "Powdery Mildew produces white powder-like fungal growth on leaves, reducing photosynthesis and plant vigor.",
    "cause": "Caused by Podosphaera xanthii and related fungi under warm days and humid nights.",
    "prevention": [
        "Improve air circulation.",
        "Avoid overcrowding.",
        "Remove infected leaves.",
        "Avoid excessive nitrogen fertilizer."
    ],
    "organic": [
        "Neem oil spray.",
        "Milk spray (1:10 dilution).",
        "Potassium bicarbonate spray."
    ],
    "chemical": [
        "Sulfur fungicide",
        "Myclobutanil",
        "Propiconazole"
    ]
},
"Strawberry___Leaf_scorch": {
    "diagnosis": "Leaf Scorch causes small purple spots that enlarge into dry brown patches, reducing leaf health.",
    "cause": "Caused by Diplocarpon earlianum under warm and humid conditions.",
    "prevention": [
        "Remove infected leaves.",
        "Avoid overhead irrigation.",
        "Ensure proper spacing.",
        "Practice crop rotation."
    ],
    "organic": [
        "Neem oil spray.",
        "Copper-based organic fungicide.",
        "Improve soil health with compost."
    ],
    "chemical": [
        "Captan",
        "Mancozeb",
        "Copper Oxychloride"
    ]
},
"Strawberry___healthy": {
    "diagnosis": "No disease detected. Strawberry plant appears healthy.",
    "cause": "Leaves are healthy without visible disease symptoms.",
    "prevention": [
        "Maintain proper irrigation.",
        "Use mulch around plants.",
        "Remove old leaves regularly.",
        "Monitor plants frequently."
    ],
    "organic": [
        "Organic compost.",
        "Seaweed extract.",
        "Vermicompost."
    ],
    "chemical": [
        "No chemical treatment required."
    ]
},
"Tomato___Bacterial_spot": {
    "diagnosis": "Bacterial Spot causes small dark water-soaked lesions on leaves, stems, and fruits, reducing fruit quality and yield.",
    "cause": "Caused by Xanthomonas species, which spread through infected seeds, rain splash, and contaminated tools.",
    "prevention": [
        "Use certified disease-free seeds.",
        "Avoid overhead irrigation.",
        "Remove infected leaves and plants.",
        "Rotate crops every season."
    ],
    "organic": [
        "Neem oil spray.",
        "Copper-based organic bactericide.",
        "Maintain good field sanitation."
    ],
    "chemical": [
        "Copper Oxychloride",
        "Copper Hydroxide",
        "Mancozeb (recommended dosage)"
    ]
},
"Tomato___Early_blight": {
    "diagnosis": "Early Blight produces brown concentric target-like lesions on older leaves, causing premature leaf drop.",
    "cause": "Caused by Alternaria solani, which survives in infected crop debris and spreads under warm, humid conditions.",
    "prevention": [
        "Practice crop rotation.",
        "Remove infected leaves.",
        "Avoid overhead irrigation.",
        "Maintain proper plant spacing."
    ],
    "organic": [
        "Neem oil spray.",
        "Trichoderma biofungicide.",
        "Compost tea application."
    ],
    "chemical": [
        "Chlorothalonil",
        "Mancozeb",
        "Azoxystrobin"
    ]
},
"Tomato___healthy": {
    "diagnosis": "No disease detected. Tomato plant appears healthy.",
    "cause": "Leaves are healthy with no visible symptoms of disease.",
    "prevention": [
        "Maintain balanced fertilization.",
        "Water plants regularly.",
        "Monitor for pests and diseases.",
        "Keep the field weed-free."
    ],
    "organic": [
        "Organic compost.",
        "Seaweed extract.",
        "Biofertilizers."
    ],
    "chemical": [
        "No chemical treatment required."
    ]
},
"Tomato___Late_blight": {
    "diagnosis": "Late Blight causes large dark water-soaked lesions on leaves, stems, and fruits, spreading rapidly during cool and humid weather.",
    "cause": "Caused by Phytophthora infestans, an aggressive water mold that spreads quickly under favorable conditions.",
    "prevention": [
        "Remove infected leaves immediately.",
        "Avoid overhead irrigation.",
        "Maintain proper spacing for airflow.",
        "Use disease-free seedlings."
    ],
    "organic": [
        "Neem oil spray.",
        "Copper-based organic fungicide.",
        "Destroy infected plant debris."
    ],
    "chemical": [
        "Metalaxyl + Mancozeb",
        "Copper Oxychloride",
        "Chlorothalonil"
    ]
},
"Tomato___Leaf_Mold": {
    "diagnosis": "Leaf Mold appears as yellow patches on the upper leaf surface with olive-green fungal growth underneath.",
    "cause": "Caused by Passalora fulva, which develops under high humidity and poor air circulation.",
    "prevention": [
        "Improve ventilation.",
        "Avoid excessive humidity.",
        "Remove infected leaves.",
        "Water plants at the base."
    ],
    "organic": [
        "Neem oil spray.",
        "Copper fungicide.",
        "Maintain proper spacing."
    ],
    "chemical": [
        "Chlorothalonil",
        "Mancozeb",
        "Azoxystrobin"
    ]
},
"Tomato___Septoria_leaf_spot": {
    "diagnosis": "Septoria Leaf Spot causes numerous small circular gray spots with dark borders, leading to premature leaf drop and reduced fruit production.",
    "cause": "Caused by the fungus Septoria lycopersici, which spreads rapidly during warm, wet weather through splashing water.",
    "prevention": [
        "Remove infected leaves immediately.",
        "Avoid overhead irrigation.",
        "Maintain proper spacing between plants.",
        "Rotate crops regularly."
    ],
    "organic": [
        "Neem oil spray.",
        "Copper-based organic fungicide.",
        "Apply compost tea to improve plant health."
    ],
    "chemical": [
        "Chlorothalonil",
        "Mancozeb",
        "Copper Oxychloride"
    ]
},
"Tomato___Spider_mites Two-spotted_spider_mite": {
    "diagnosis": "Two-spotted Spider Mites feed on leaf sap, causing yellow speckles, webbing, leaf drying, and reduced plant vigor.",
    "cause": "Caused by infestation of Tetranychus urticae, especially under hot and dry weather conditions.",
    "prevention": [
        "Inspect leaves regularly.",
        "Increase humidity around plants.",
        "Remove heavily infested leaves.",
        "Keep plants well-watered."
    ],
    "organic": [
        "Neem oil spray.",
        "Insecticidal soap.",
        "Release predatory mites where available."
    ],
    "chemical": [
        "Abamectin",
        "Spiromesifen",
        "Bifenazate"
    ]
},
"Tomato___Target_Spot": {
    "diagnosis": "Target Spot produces circular brown lesions with concentric rings on leaves and fruits, reducing yield significantly.",
    "cause": "Caused by the fungus Corynespora cassiicola under warm and humid environmental conditions.",
    "prevention": [
        "Remove infected plant debris.",
        "Avoid overhead irrigation.",
        "Improve air circulation.",
        "Practice crop rotation."
    ],
    "organic": [
        "Neem oil spray.",
        "Copper fungicide.",
        "Trichoderma biofungicide."
    ],
    "chemical": [
        "Azoxystrobin",
        "Chlorothalonil",
        "Mancozeb"
    ]
},
"Tomato___Tomato_mosaic_virus": {
    "diagnosis": "Tomato Mosaic Virus causes mottled light and dark green leaves, leaf distortion, stunted growth, and poor fruit development.",
    "cause": "Caused by Tomato Mosaic Virus (ToMV), which spreads through infected seeds, contaminated tools, and plant handling.",
    "prevention": [
        "Use certified virus-free seeds.",
        "Disinfect tools regularly.",
        "Remove infected plants immediately.",
        "Avoid handling plants after tobacco use."
    ],
    "organic": [
        "Maintain field hygiene.",
        "Use healthy seedlings.",
        "Control insect vectors if present."
    ],
    "chemical": [
        "No effective chemical treatment available.",
        "Focus on prevention and sanitation."
    ]
},
"Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
    "diagnosis": "Tomato Yellow Leaf Curl Virus causes upward curling leaves, yellowing, stunted growth, and severe reduction in fruit production.",
    "cause": "Caused by Tomato Yellow Leaf Curl Virus (TYLCV), primarily transmitted by whiteflies.",
    "prevention": [
        "Control whitefly populations.",
        "Use resistant tomato varieties.",
        "Remove infected plants promptly.",
        "Keep fields free from weeds that may host the virus."
    ],
    "organic": [
        "Neem oil spray to suppress whiteflies.",
        "Use yellow sticky traps.",
        "Release beneficial insects where appropriate."
    ],
    "chemical": [
        "Imidacloprid",
        "Thiamethoxam",
        "Apply insecticides only according to agricultural recommendations."
    ]
}
}

DEFAULT_REMEDY = {
    "diagnosis": "The uploaded plant disease could not be identified with confidence. Please upload a clear image of a single leaf under good lighting.",
    
    "cause": "The detected class is unavailable in the current PlantVillage remedy database or the prediction confidence is too low.",

    "prevention": [
        "Capture a clear image of one leaf only.",
        "Ensure good natural lighting.",
        "Avoid blurry or partially visible leaves.",
        "Monitor the plant regularly for any visible symptoms."
    ],

    "organic": [
        "Maintain proper irrigation and drainage.",
        "Apply well-decomposed organic compost.",
        "Use neem oil as a preventive measure.",
        "Remove damaged or diseased leaves if present."
    ],

    "chemical": [
        "Do not apply pesticides or fungicides until the disease is correctly identified.",
        "Consult a local agricultural expert if symptoms persist."
    ]
}

def get_remedy(class_name):
    return REMEDIES.get(class_name, DEFAULT_REMEDY)