import os
import face_recognition

image_path = os.path.join(os.environ.get("INPUT_DIR"), 'test', 'test_image.jpg')

image = face_recognition.load_image_file(image_path)
face_landmarks_list = face_recognition.face_landmarks(image)
print(face_landmarks_list)