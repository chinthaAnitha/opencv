import cv2
import numpy as np
kernal=np.ones((5,5),np.uint8)
im=cv2.imread('C:\\Users\\anitha chintha\\Downloads\\mouse.jpg',1)
#cv2.namedWindow("img",cv2.WINDOW_NORMAL)
cv2.imshow("img",im)
imgray=cv2.cvtColor(im,cv2.COLOR_YUV2BGR)
imcanny=cv2.Canny(im,100,100)
cv2.imshow("AFTER",imgray)
cv2.imshow("canny",imcanny)
imb=cv2.GaussianBlur(im,(5,5),3)
cv2.imshow("blur",imb)
print(im.shape)
imgc=im[0:100,100:200]
cv2.imshow("crop",imgc)
imgd=cv2.dilate(im,kernal,iterations=1)
imge=cv2.erode(im,kernal,iterations=1)
cv2.imshow("dialte",imgd)
cv2.imshow("erode",imge)
cv2.waitKey(0)
cv2.destroyAllWindows()