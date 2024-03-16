import tkinter

import face_recognition
import cv2
import numpy as np
import csv
from tkinter import *
import tkinter as tk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import *
import pickle
from PIL import Image, ImageTk
import time
root = Tk()
Captures=[]
def showattendance():
    try:
        Label(root, text=Captures, justify='left').grid(row=12, column=7)
    except:
        Label(root, text=Captures).pack()



def Inputtext():
    def printInput():
        global filename
        inp = inputtxt.get(1.0, "end-1c")
        filename = inp
        lbl.config(text="Provided Input: " + inp)


    # TextBox Creation
    inputtxt = tk.Text(root,
                       height=5,
                       width=20)

    inputtxt.pack()

    # Button Creation
    printButton = tk.Button(root,
                            text="Print",
                            command=printInput)

    printButton.pack()

    # Label Creation
    lbl = tk.Label(root, text="")
    lbl.pack()

def Close():
    video_capture.release()
    cv2.destroyAllWindows()
    f.close()
    root.destroy()


def newuser():
    Label(root, text="THIS BUTTON IS UNDER CONSTRUCTION").pack()

def capture():
    Label(root, text="THIS BUTTON IS UNDER CONSTRUCTION").pack()

def help():
    Label(root, text="THIS BUTTON IS UNDER CONSTRUCTION").pack()

root.geometry("1200x720")
root.title("Face Attendance System")
root.configure(bg="black")
# frame1=tkinter.Frame(root)
# frame1.pack(side=tk.LEFT,padx=20)
Label(root, text="ATTENDANCE SYSTEM", font=("Algerian", 22, "bold"), bg="white", fg="black").pack()
f1 = LabelFrame(root, bg="white")
f1.pack()
L1 = Label(f1, bg="blue")
L1.pack()
b1=Button(root,text="Show attenendance",font=('algerian',14),bg='cyan2',fg='white',command=showattendance)
b1.place(x=100,y=110)
b2=Button(root,text="Filename",font=('algerian',14),bg='cyan2',fg='white',command=Inputtext)
b2.place(x=100,y=160)
b3=Button(root,text="Capture",font=('algerian',14),bg='cyan2',fg='white',command=capture)
b3.place(x=100,y=60)
b6=Button(root,text="close",font=('algerian',14),bg='cyan2',fg='white',command=Close)
b6.place(x=1100,y=160)
b4=Button(root,text="New user",font=('algerian',14),bg='cyan2',fg='white',command=newuser)
b4.place(x=1100,y=60)
b5=Button(root,text="Help",font=('algerian',14),bg='cyan2',fg='white',command=help)
b5.place(x=1100,y=110)






print("Loading Encoded file .......")
file = open('Encodefile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
known_face_encodings, known_face_names = encodeListKnownWithIds
# print(studentIds)
print("Encoded file Loaded successfully ")





cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-a92d4-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-a92d4.appspot.com"
})

bucket = storage.bucket()




# print(known_face_encodings)
video_capture = cv2.VideoCapture(0)
# List of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []
# Get the current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", "w+", newline="")
lnwter=csv.writer(f)

while True:
    ret, frame = video_capture.read()
    imgs = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imgs = ImageTk.PhotoImage(Image.fromarray(imgs))
    L1['image'] = imgs

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            print(known_face_names[best_match_index])
            studentInfo = db.reference(f'Student/{name}').get()
            print(studentInfo)
            Captures=[studentInfo]
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, 100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness,
                            lineType)
            if name in students:
                students.remove(name)
                current_time = time.strftime("%H:%M:%S")
                lnwter.writerow([studentInfo['Name'],studentInfo['Batch'],studentInfo['Rollno'],studentInfo['PRN No'], current_time])

    # cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    root.update()

video_capture.release()
cv2.destroyAllWindows()
f.close()
input("ENTER TO CLOSE")