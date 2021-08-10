import cv2
video=cv2.VideoCapture('C:\\Users\\anitha chintha\\Downloads\\ntr.mp4')
while True:
    val,img=video.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) &0xff==ord('q'):
        break