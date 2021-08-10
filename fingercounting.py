import cv2
import time
import os
import handtracking as ht
#ptime=0


cap=cv2.VideoCapture(0)
cap.set(3,1020)
cap.set(4,680)

folderpath='C:\\Users\\anitha chintha\\Downloads\\fingers'
mylist=os.listdir(folderpath)
print(mylist)
overlaylist=[]

detector=ht.handdetector(detectcon=0.5)
for impath in mylist:
    image=cv2.imread(f'{folderpath}/{impath}')
    img=cv2.resize(image,(200,200))
    #print(f'{folderpath}/{impath}')
    overlaylist.append(img)
print(len(overlaylist))


tipids=[4,8,12,16,20]
ctime,ptime=0,0


while True:
    
    val,img=cap.read()
    img=detector.findhands(img)
    lmlist=detector.findposition(img,draw=False)
    #print(lmlist)
    if len(lmlist)!=0:
        fingers=[]
        if lmlist[tipids[0]][1] <lmlist[tipids[0]-1][1]:
            fingers.append(1)
                #print("index finger open")
        else:
            fingers.append(0)
        for id in range(1,5):
            if lmlist[tipids[id]][2] <lmlist[tipids[id]-2][2]:
                fingers.append(1)
                #print("index finger open")
            else:
                fingers.append(0)
        #print(fingers)
            total=fingers.count(1)
        print(total)

        h,w,c=overlaylist[total-1].shape
        img[0:h,0:w]=overlaylist[total-1]
        cv2.rectangle(img,(20,225),(178,425),(255,255,0),cv2.FILLED)
        cv2.putText(img,str(total),(45,375),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(255,0,0),5)




    
        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime
        cv2.putText(img,f'FPS:{int(fps)}',(480,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),4)


    cv2.imshow("video",img)
    if cv2.waitKey(1)& 0xff==ord('q'):
        break