from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2


frames = 20
FPS = 10
size = (640, 480)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,size[0])
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,size[1])
cap.set(cv2.CAP_PROP_FPS, FPS)
start = time.time()
img_array = []
for i in range(frames):
    ret, img = cap.read()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display the output
    # cv2.imshow('img', img)
    # cv2.waitKey()
    img_array.append(img)
    # cv2.imwrite("output{}.jpg".format(i), img) 
print("Time for {0} frames: {1} seconds".format(frames, time.time() - start))
out = cv2.VideoWriter('detected.avi',cv2.VideoWriter_fourcc(*'DIVX'), FPS, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
