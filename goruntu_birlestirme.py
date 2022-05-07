import cv2
import numpy as np
import os

img1_path=os.path.join(os.getcwd(),"images","chp2","nature.jpg")
img2_path=os.path.join(os.getcwd(),"images","chp2","zebrasmall.png")

img1=cv2.imread(img1_path)
img2=cv2.imread(img2_path)

r_img1=cv2.resize(img1,(300,300),interpolation=cv2.INTER_AREA)
r_img2=cv2.resize(img2,(300,300),interpolation=cv2.INTER_AREA)

add_1=cv2.add(r_img2,r_img1)
add_2 = cv2.addWeighted(r_img1,0.7,r_img2,0.3,0)

cv2.imshow("ekleme 1", add_1)
cv2.imshow("ekleme 2", add_2)
cv2.imshow("resim 1", img1)
cv2.imshow("resim 2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
