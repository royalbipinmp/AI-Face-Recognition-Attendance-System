import cv2
import numpy as np
import os
import csv
from datetime import datetime

# Load trained model
model = cv2.face.LBPHFaceRecognizer_create()
model.read("models/face_model.yml")

# Name list (same order as training)
names = os.listdir("datasets/")

# Haarcascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Attendance file
attendance_file = "attendance.csv"

# Create file if not exists
if not os.path.exists(attendance_file):
    with open(attendance_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Date", "Time"])

# Function to mark attendance
def mark_attendance(name):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    # Avoid marking twice on same day
    with open(attendance_file, "r") as f:
        data = f.readlines()

    for line in data:
        if name in line and date in line:
            return  # Already present today

    with open(attendance_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, date, time])
        print(f"✔ Attendance marked for {name}")

# Start webcam
cam = cv2.VideoCapture(0)

print("📷 Starting Attendance System... Press Q to Quit")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces_detected = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces_detected:
        face = gray[y:y+h, x:x+w]
        resized_face = cv2.resize(face, (200, 200))

        label, confidence = model.predict(resized_face)

        if confidence < 80:
            name = names[label]
            mark_attendance(name)
            text = f"{name} ({int(confidence)})"
        else:
            text = "Unknown"

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, text, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
