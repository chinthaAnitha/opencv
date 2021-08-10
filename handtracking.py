import cv2
import mediapipe as mp
import time
ptime=0
class handdetector():
    def __init__(self,mode=False,maxhands=2,detectcon=0.5,detecttrac=0.5):
        self.mode=mode
        self.maxhands=maxhands
        self.detectcon=detectcon
        self.detecttrac=detecttrac
        self.mphands=mp.solutions.hands
        #hands is object for mphands
        self.hands=self.mphands.Hands(self.mode,self.maxhands,self.detectcon,self.detecttrac)
        self.mpdraw=mp.solutions.drawing_utils
    def findhands(self,img,draw=True):
        imggrb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        #for processing the imgrgb
        self.result=self.hands.process(imggrb)
        #print(self.result.multi_hand_landmarks)
        if self.result.multi_hand_landmarks:
            for handlms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img,handlms,self.mphands.HAND_CONNECTIONS)
        return img
    def findposition(self,img,handno=0,draw=True):

        lmlist=[]  #landmark list
        if self.result.multi_hand_landmarks:
            myhand=self.result.multi_hand_landmarks[handno] 
            for id,lm in enumerate(myhand.landmark):
                #print(id,lm)
                h,w,c=img.shape  #height ,width,channel
                cx,cy=int(lm.x*w),int(lm.y*h) # x,y,z are in flaoting points to convert into into pixel we have to multiply into widrh ,height
                #print(id,cx,cy)
                    #if id==4:
                lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),5,(255,0,0),4)
        return lmlist
def main():
    
    cap=cv2.VideoCapture(0)
    detector=handdetector()
    while True:
        ctime,ptime=0,0
        val,img=cap.read()
        img=detector.findhands(img)
        lmlist=detector.findposition(img)
        if len(lmlist)!=0:
            print(lmlist[4])
        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime
        cv2.putText(img,f'FPS:{int(fps)}', (10,70), cv2.FONT_HERSHEY_COMPLEX, 2,(255,0,0),2)
        cv2.imshow("video",img)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break
if __name__=='__main__':
    main()