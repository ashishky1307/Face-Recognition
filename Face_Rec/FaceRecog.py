import face_recognition
import cv2
import numpy as np
import csv
from tkinter import *
# import tkinter as tk
from datetime import *
import cvzone

from PIL import Image, ImageTk

root = Tk()

root.geometry("1200x720")
root.configure(bg="black")
Label(root, text="ATTENDANCE SYSTEM", font=("Algerin", 22, "bold"), bg="white", fg="black").pack()
f1 = LabelFrame(root, bg="white")
f1.pack()
L1 = Label(f1, bg="blue")
L1.pack()

video_capture = cv2.VideoCapture(0)
# Akshata_image = face_recognition.load_image_file("faces/404.jpg")
# Akshata_encoding = face_recognition. face_encodings (Akshata_image)[0]

Aditya_image = face_recognition.load_image_file("faces/403.jpg")
Aditya_encoding = face_recognition.face_encodings(Aditya_image)[0]

Shubham_image = face_recognition.load_image_file("faces/404.jpg")
Shubham_encoding = face_recognition.face_encodings(Shubham_image)[0]

Ankita_image = face_recognition.load_image_file("faces/405.png")
Ankita_encoding = face_recognition.face_encodings(Ankita_image)[0]

Gyanesh_image = face_recognition.load_image_file("faces/406.png")
Gyanesh_encoding = face_recognition.face_encodings(Gyanesh_image)[0]

# Prathamesh_image = face_recognition.load_image_file("faces/404.jpg")
# Prathamesh_image = face_recognition. face_encodings (Prathamesh_image)[0]

Sanket_image = face_recognition.load_image_file("faces/408.jpg")
Sanket_encoding = face_recognition.face_encodings(Sanket_image)[0]

known_face_encodings = [Sanket_encoding, Shubham_encoding, Aditya_encoding, Ankita_encoding, Gyanesh_encoding]

known_face_names = ["408", "404", "403", "405", "407"]
# List of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []
# Get the current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
    ret, frame = video_capture.read()
    imgs=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    imgs=ImageTk.PhotoImage(Image.fromarray(imgs))
    L1['image']=imgs


    small_frame = cv2.resize(frame, (0, 0),fx=0.25,fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)


    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if (matches[best_match_index]):
            name = known_face_names[best_match_index]
        # Add text if a person is present
        # if name in known_face_names:
        #     y1, x2, y2, x1 = face_locations
        #     y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        #     bbox = 2 + x1, 2 + y1, x2 - x1, y2 - y1
        #     frame = cvzone.cornerRect(frame, bbox, rt=0)
            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])

    # cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    root.update()

video_capture.release()
cv2.destroyAllWindows()
f.close()
