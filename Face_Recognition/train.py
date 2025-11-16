import os
import cv2
import numpy as np

data_path = "datasets/"

labels = []
faces = []
label_id = 0

# Set fixed image size
IMG_SIZE = (200, 200)

for person in os.listdir(data_path):
    person_path = os.path.join(data_path, person)

    if not os.path.isdir(person_path):
        continue

    print(f"✔️ Loading images for: {person}")

    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)

        img = cv2.imread(img_path)

        if img is None:
            continue

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Resize every image to SAME size
        resized = cv2.resize(gray, IMG_SIZE)

        faces.append(resized)
        labels.append(label_id)

    label_id += 1

# Convert to numpy arrays
faces = np.array(faces)
labels = np.array(labels)

print("\n⏳ Training model...")

# Create LBPH model
model = cv2.face.LBPHFaceRecognizer_create()
model.train(faces, labels)

# Save model
os.makedirs("models", exist_ok=True)
model.save("models/face_model.yml")

print("\n✅ Training complete! Model saved at: models/face_model.yml")
