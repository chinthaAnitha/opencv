import cv2
import mediapipe as mp
import os
import time
cap=cv2.VideoCapture('C:\\Users\\anitha chintha\\Downloads\\santhi.mp4')
mpdraw=mp.solutions.drawing_utils
myface=mp.solutions.face_mesh
facemesh=myface.FaceMesh()
while True:
    ctime=0
    ptime=0
    val,img=cap.read()
    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img, f'fps:{int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0),4)
    cv2.imshow("video",img)
    if cv2.waitKey(100)&0xff==ord('q'):
        break