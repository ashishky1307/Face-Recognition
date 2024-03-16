import face_recognition
import cv2
import pickle
import os

# adding student images to list
folderpath = "faces"
pathlist = os.listdir(folderpath)
studentIds = []
imagelist = []
for path in pathlist:
    imagelist.append(cv2.imread(os.path.join(folderpath, path)))
    studentIds.append(os.path.splitext(path)[0])  # tuples first element of returened value of splittext()


# print(len(imagelist))
# print(studentIds)

def findEncodings(imageslist):
    encodeList = []
    for img in imageslist:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


print("ENCODING Started .......")
encodeListKnown=findEncodings(imagelist)
encodeListKnownWithIds=[encodeListKnown,studentIds]
print("ENCODING Completed")

file=open("Encodefile.p", "wb")
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("File Saved Succesfully")