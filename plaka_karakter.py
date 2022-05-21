import cv2
from cv2 import imshow
import numpy as np
import os

# yol = os.path.join(os.getcwd(),"images","chp2","rice_1.jpg")
yol = os.path.join(os.getcwd(),"images","chp2","plaka.jpg")
goruntu=cv2.imread(yol)

# gri tonlama
gri =cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
# bulanık(blur)
bulanik = cv2.GaussianBlur(gri,(11,11),0)

canny = cv2.Canny(bulanik,40,180)

# konturları bulma(yani kontur olan piksellerin listesini bulma)
konturlar,_ = cv2.findContours(canny, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
i=0

for kontur in konturlar[0:12]:
    (x,y,w,h)=cv2.boundingRect(kontur)
    alan=cv2.contourArea(kontur)
    if alan>1000 and alan<5000:
        i=i+1
        r=goruntu[y:y+h,x:x+w]
        imshow(str(i)+"--"+str(alan),r)
    


print(i)



cv2.imshow("orijinal",goruntu)
# # cv2.imshow("gri",gri)
# # cv2.imshow("sb",sb)
# # cv2.imshow("sba",sba)
# cv2.imshow("canny",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()