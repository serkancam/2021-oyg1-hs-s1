import cv2
import os
import numpy as np


dosya_yolu=os.path.join(os.getcwd(),"images","chp2","zebra.png")
img=cv2.imread(dosya_yolu)

h,w,c = img.shape
aspect=w/h
# h1=int(h*2.5)
h1=300
w1=int(h1*aspect)
boyut=(w1,h1)

yeni1=cv2.resize(img,boyut,interpolation=cv2.INTER_AREA)
yeni2=cv2.resize(img,boyut,interpolation=cv2.INTER_LANCZOS4)
yeni3=cv2.resize(src=img,dsize=None,fx=0.8,fy=0.8,interpolation=cv2.INTER_LINEAR)

cv2.imshow("kucuk resim1",yeni1)
cv2.imshow("kucuk resim2",yeni2)
cv2.imshow("kucuk resim3",yeni3)
cv2.imshow("orijinal",img)
cv2.waitKey(0)
cv2.destroyAllWindows()