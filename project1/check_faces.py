import face_recognition
import os

KNOWN_FACES_DIR = "/home/atai/Desktop/project1/known_faces"

for filename in os.listdir(KNOWN_FACES_DIR):
    image_path = os.path.join(KNOWN_FACES_DIR, filename)
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)

    if encodings:
        print(f"✅ Face found in {filename}")
    else:
        print(f"❌ No face detected in {filename}")
