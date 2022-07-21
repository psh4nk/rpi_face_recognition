import face_recognition
import os

# Before running this program, a directory named "dataset/your_name"
# populated with multiple .jpg images of the same individual must be
# created in the same directory as this program.

subdir = "dataset/Chuck/"
face_images = []

for file in os.listdir(subdir):
        if file.endswith(".jpg"):
            image = face_recognition.load_image_file(subdir+file)
            try:
                image_to_be_matched_encoded = face_recognition.face_encodings(image)[0]
                print("Face found in image: " + os.path.join(subdir, file))
                face_images.append(os.path.join(subdir, file))
            except IndexError as e:
                print("No face found in image: " + os.path.join(subdir, file))

print("Images ready for face recognition usage: ")

for image in face_images:
    print(image)
