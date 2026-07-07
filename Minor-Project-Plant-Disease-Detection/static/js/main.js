// Frontend Interactivity for AgriShield AI Dashboard
let selectedFile = null;
let stream = null;
let currentInputMode = 'upload'; // 'upload' or 'camera'

// DOM Elements
const uploadBox = document.getElementById('uploadBox');
const cameraBox = document.getElementById('cameraBox');
const fileInput = document.getElementById('fileInput');
const dropZone = document.getElementById('dropZone');
const imagePreview = document.getElementById('imagePreview');
const previewContainer = document.getElementById('previewContainer');
const webcamVideo = document.getElementById('webcamVideo');
const webcamCanvas = document.getElementById('webcamCanvas');
const cameraPlaceholder = document.getElementById('cameraPlaceholder');
const cameraControls = document.getElementById('cameraControls');

const emptyState = document.getElementById('emptyState');
const resultsContent = document.getElementById('resultsContent');
const loaderSpinner = document.getElementById('loaderSpinner');
const loaderSeedling = document.getElementById('loaderSeedling');
const emptyTitle = document.getElementById('emptyTitle');
const emptyText = document.getElementById('emptyText');



// Toggle Input Modes (Upload File vs Camera)
function setInputMode(mode) {
    currentInputMode = mode;
    document.getElementById('modeUploadBtn').classList.toggle('active', mode === 'upload');
    document.getElementById('modeCameraBtn').classList.toggle('active', mode === 'camera');
    
    if (mode === 'upload') {
        uploadBox.classList.add('active');
        cameraBox.classList.remove('active');
        stopWebcam();
    } else {
        uploadBox.classList.remove('active');
        cameraBox.classList.add('active');
        clearPreview();
    }
}

// Drag & Drop Event Listeners
['dragenter', 'dragover'].forEach(eventName => {
    dropZone.addEventListener(eventName, e => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    }, false);
});

['dragleave', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, e => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
    }, false);
});

dropZone.addEventListener('drop', e => {
    const dt = e.dataTransfer;
    const files = dt.files;
    if (files.length > 0) {
        handleFileSelect(files[0]);
    }
});

fileInput.addEventListener('change', e => {
    if (e.target.files.length > 0) {
        handleFileSelect(e.target.files[0]);
    }
});

function handleFileSelect(file) {
    if (!file.type.startsWith('image/')) {
        alert("Please upload an image file.");
        return;
    }
    selectedFile = file;
    const reader = new FileReader();
    reader.onload = function(e) {
        imagePreview.src = e.target.result;
        previewContainer.style.display = "flex";
        uploadBox.style.display = "none";
    }
    reader.readAsDataURL(file);
}

// Webcam stream controls
async function initWebcam() {
    try {
        cameraPlaceholder.style.display = "none";
        
        const constraints = {
            video: {
                width: { ideal: 640 },
                height: { ideal: 480 },
                facingMode: "environment" // Prefer rear camera on mobile
            },
            audio: false
        };
        
        stream = await navigator.mediaDevices.getUserMedia(constraints);
        webcamVideo.srcObject = stream;
        cameraControls.style.display = "flex";
    } catch (err) {
        console.error("Camera access error:", err);
        alert("Could not access webcam. Please verify camera permissions or upload a file instead.");
        cameraPlaceholder.style.display = "flex";
        cameraControls.style.display = "none";
    }
}

function stopWebcam() {
    if (stream) {
        stream.getTracks().forEach(track => track.stop());
        stream = null;
    }
    webcamVideo.srcObject = null;
    cameraPlaceholder.style.display = "flex";
    cameraControls.style.display = "none";
}

function capturePhoto() {
    if (!stream) return;
    
    // Size matching video stream size
    webcamCanvas.width = webcamVideo.videoWidth;
    webcamCanvas.height = webcamVideo.videoHeight;
    
    const ctx = webcamCanvas.getContext('2d');
    // Draw mirrored image if facing user
    ctx.drawImage(webcamVideo, 0, 0, webcamCanvas.width, webcamCanvas.height);
    
    const dataUrl = webcamCanvas.toDataURL('image/jpeg');
    imagePreview.src = dataUrl;
    
    // Stop camera stream since capture is done
    stopWebcam();
    
    // Set file to base64 string placeholder
    selectedFile = dataUrl; // Save base64 string
    
    previewContainer.style.display = "flex";
    cameraBox.style.display = "none";
}

// Clear Preview
function clearPreview() {
    selectedFile = null;
    imagePreview.src = "";
    previewContainer.style.display = "none";
    
    if (currentInputMode === 'upload') {
        uploadBox.style.display = "block";
    } else {
        cameraBox.style.display = "block";
        cameraPlaceholder.style.display = "flex";
        cameraControls.style.display = "none";
    }
}

// Fetch Sample from Server and Run Analysis immediately
async function loadSample(className) {
    clearPreview();
    setLoadingState(true, "Fetching sample image...");
    
    try {
        const sampleUrl = `/static/samples/${className}.jpg`;
        const res = await fetch(sampleUrl);
        if (!res.ok) throw new Error("Failed to load image");
        
        const blob = await res.blob();
        
        // Setup image preview
        selectedFile = new File([blob], `${className}.jpg`, { type: "image/jpeg" });
        const reader = new FileReader();
        reader.onload = function(e) {
            imagePreview.src = e.target.result;
            previewContainer.style.display = "flex";
            if (currentInputMode === 'upload') {
                uploadBox.style.display = "none";
            } else {
                cameraBox.style.display = "none";
            }
            
            // Run inference automatically for samples
            runInference();
        };
        reader.readAsDataURL(blob);
    } catch (err) {
        console.error(err);
        alert("Error loading sample leaf image.");
        setLoadingState(false);
    }
}

// Loading Animation Manager
function setLoadingState(isLoading, message = "") {
    if (isLoading) {
        loaderSeedling.style.display = "none";
        loaderSpinner.style.display = "block";
        emptyTitle.innerText = message || "Processing Image...";
        emptyText.innerText = "Extracting leaf morphology features and passing through CNN layers...";
        emptyState.style.display = "flex";
        resultsContent.style.display = "none";
    } else {
        loaderSpinner.style.display = "none";
        loaderSeedling.style.display = "block";
    }
}

// Run Inference API
async function runInference() {
    if (!selectedFile) {
        alert("Please upload or capture a leaf first.");
        return;
    }
    
    setLoadingState(true, "Scanning Leaf Pathology...");
    
    const formData = new FormData();
    if (typeof selectedFile === 'string') {
        // Base64 string from webcam
        formData.append('image', selectedFile);
    } else {
        // File Object from upload
        formData.append('file', selectedFile);
    }
    
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.error || "Server error occurred");
        }
        
        const data = await response.json();
        displayResults(data);
    } catch (err) {
        console.error("Inference Error:", err);
        alert(err.message || "Failed to analyze image. Please try again.");
        emptyTitle.innerText = "Scan Failed";
        emptyText.innerText = "We ran into an error processing your leaf. Please ensure it is a valid leaf photo and try again.";
        setLoadingState(false);
    }
}

// Display Results & Remedies in DOM
function displayResults(data) {
    setLoadingState(false);
    emptyState.style.display = "none";
    resultsContent.style.display = "block";
    
    // 1. Update Name and Confidence
    const confidencePct = Math.round(data.confidence * 100);
    document.getElementById('predictionName').innerText = data.display_name;
    document.getElementById('predictionConfidence').innerText = `${confidencePct}%`;
    document.getElementById('predictionPercentageText').innerText = `${(data.confidence * 100).toFixed(2)}%`;
    
    // Set Status Badge
    const isHealthy = data.class.endsWith('_healthy');
    const badge = document.getElementById('healthStatusBadge');
    if (isHealthy) {
        badge.innerText = "Healthy";
        badge.className = "badge healthy";
    } else {
        badge.innerText = "Infected";
        badge.className = "badge";
    }
    
    // 2. Set Circular Progress Ring Offset
    // r=42, circumference=263.89
    const ringFill = document.getElementById('ringFillProgress');
    const strokeDasharray = 263.89;
    const strokeDashoffset = strokeDasharray - (strokeDasharray * data.confidence);
    ringFill.style.strokeDashoffset = strokeDashoffset;
    
    // Shift color of circular ring based on health/confidence
    if (isHealthy) {
        ringFill.style.stroke = "var(--accent-green)";
    } else if (data.confidence < 0.6) {
        ringFill.style.stroke = "var(--accent-orange)";
    } else {
        ringFill.style.stroke = "var(--accent-red)";
    }

    
        
    document.getElementById("remedyDiagnosis").innerHTML =
        data.remedy.diagnosis;

    document.getElementById("remedyCause").innerHTML =
        data.remedy.cause;

    fillRemedyList("remedyPreventionList", data.remedy.prevention);

    fillRemedyList("remedyOrganicList", data.remedy.organic);

    fillRemedyList("remedyChemicalList", data.remedy.chemical);


    // Automatically open first accordion tab
    document.querySelectorAll('.accordion-item').forEach(item => {
        item.classList.remove('open');
    });

    document.getElementById('accItemDiagnosis').classList.add('open');

    // Scroll result panel into view
    document.getElementById('resultsPanel').scrollIntoView({
        behavior: 'smooth'
    });

    }
    

function fillRemedyList(elementId, itemsList) {
    const listEl = document.getElementById(elementId);
    listEl.innerHTML = '';
    if (itemsList && itemsList.length > 0) {
        itemsList.forEach(item => {
            const li = document.createElement('li');
            li.innerHTML = item;
            listEl.appendChild(li);
        });
    } else {
        const li = document.createElement('li');
        li.innerText = "No specific items recommended.";
        li.style.color = "var(--text-muted)";
        li.style.fontStyle = "italic";
        li.style.paddingLeft = "0px";
        li.classList.add('no-bullet');
        listEl.appendChild(li);
    }
}

// Accordion Control
function toggleAccordion(itemId) {
    const item = document.getElementById(itemId);
    const isOpen = item.classList.contains('open');
    
    // Optional: Close all others (single-open behavior)
    document.querySelectorAll('.accordion-item').forEach(i => {
        i.classList.remove('open');
    });
    
    if (!isOpen) {
        item.classList.add('open');
    }
}