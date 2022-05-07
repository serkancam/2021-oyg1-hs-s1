from turtle import shape
import cv2
from matplotlib.pyplot import sca
import numpy as np
import os

img_path = os.path.join(os.getcwd(), "images", "chp2", "zebrasmall.png")
img = cv2.imread(img_path)
h, w, c = img.shape
# translation matris 
center=(h//2,w//2)
angle=-180
scale=1.0
d1=0.98
d2=1.02
d=d1
while True:
    rotation_matrix=cv2.getRotationMatrix2D(center=center,angle=angle,scale=scale)

    # dönmüş resmi oluşturalım
    rotated_img=cv2.warpAffine(img,rotation_matrix,(h,w))
    angle+=5
    if scale>1.1 and d==d2:
        d=d1
    if scale<0.1 and d==d1:
        d=d2
    scale*=d
    # görselleri gösterelim
    cv2.imshow("orijinal", img)
    cv2.imshow("rotated", rotated_img)
    if cv2.waitKey(50)==27:#("0xFF" and ord('q')):
        break
cv2.destroyAllWindows()
