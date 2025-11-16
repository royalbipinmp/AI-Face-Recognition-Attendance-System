import cv2
import os

name = input("Enter your name: ")

folder = f"datasets/{name}"
os.makedirs(folder, exist_ok=True)

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

count = 0

print("Showing camera... Look at the camera.")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        face = gray[y:y+h, x:x+w]
        cv2.imwrite(f"{folder}/{name}_{count}.jpg", face)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow("Capturing", frame)

    if cv2.waitKey(1) == ord('q') or count >= 50:
        break

cap.release()
cv2.destroyAllWindows()

print("Captured", count, "images.")
