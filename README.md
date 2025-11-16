# 📌 AI Face Recognition Attendance System

A simple and beginner-friendly Python project that uses **Face Recognition + OpenCV** to automatically mark attendance using your webcam.

---

## 🚀 Features
- Real-time face recognition  
- Capture face images using webcam  
- Train a face model  
- Auto-generate attendance.csv  
- Works for multiple users  
- Very simple code structure  

---

## 📂 Project Structure
```
Face_Recognition/
│
├── capture.py          # Capture face images
├── train.py            # Train model
├── attendance.py       # Mark attendance
├── recognize.py        # Optional live recognition
│
├── datasets/           # Face images (EMPTY in GitHub)
├── models/             # Encodings/model (EMPTY in GitHub)
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

### 1️⃣ Clone the Project
```
git clone https://github.com/your-username/AI-Face-Recognition-Attendance-System.git
cd AI-Face-Recognition-Attendance-System
```

### 2️⃣ Install Required Libraries
```
pip install -r requirements.txt
```

---

## 📸 Step 1 — Capture Face Images
Run:
```
python capture.py
```

What happens:
- Webcam opens  
- Detects your face  
- Saves 50 images into:  
  `datasets/YourName/`  
- Press **q** to quit  

---

## 🧠 Step 2 — Train the Model
Run:
```
python train.py
```

This will:
- Read images from datasets  
- Generate face encodings  
- Save to:  
  `models/encodings.pickle`  

---

## 🎥 Step 3 — Mark Attendance
Run:
```
python attendance.py
```

This will:
- Recognize your face  
- Create/update `attendance.csv`  
- Log format:
```
Name, Date, Time
Bipin, 2025-11-15, 10:24:55
```

---

## 🔐 Privacy & Security
These **should NOT be uploaded to GitHub**:

```
datasets/YourName/
models/encodings.pickle
attendance.csv
```

### Recommended `.gitignore`
```
datasets/
models/
*.csv
*.pickle
*.pkl
*.npy
__pycache__/
*.pyc
```

---

## 📝 requirements.txt
```
opencv-python
face-recognition
numpy
pandas
```

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 👨‍💻 Developed By
**Bipin M P**

---
