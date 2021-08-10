import cv2
import mediapipe as mp
import time
ptime=0
ctime=0
mphands=mp.solutions.hands
#hands is object for mphands
hands=mphands.Hands()
mpdraw=mp.solutions.drawing_utils
cap=cv2.VideoCapture(0)
while True:
    val,img=cap.read()
    
    imggrb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #for processing the imgrgb
    result=hands.process(imggrb)
    print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):
                #print(id,lm)
                h,w,c=img.shape  #height ,width,channel
                cx,cy=int(lm.x*w),int(lm.y*h) # x,y,z are in flaoting points to convert into into pixel we have to multiply into widrh ,height
                print(id,cx,cy)
                #if id==4:
                cv2.circle(img,(cx,cy),5,(255,0,0),4)

            mpdraw.draw_landmarks(img,handlms,mphands.HAND_CONNECTIONS)
    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 2,(255,0,0),2)
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break