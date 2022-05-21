import cv2
import numpy as np
import os

# yol = os.path.join(os.getcwd(),"images","chp2","rice_1.jpg")
yol = os.path.join(os.getcwd(),"images","chp2","plaka.jpg")
goruntu=cv2.imread(yol)

# gri tonlama
gri =cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
# bulanık(blur)
bulanik = cv2.GaussianBlur(gri,(3,3),0)
# eşikleme(siyah/beyaz)
# _,sb = cv2.threshold(bulanik,140,255,cv2.THRESH_BINARY)
# sba = cv2.adaptiveThreshold(bulanik,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,3)
# canny kenar tespit fonksiyonu
canny = cv2.Canny(bulanik,40,180)

# konturları bulma(yani kontur olan piksellerin listesini bulma)
konturlar,_ = cv2.findContours(canny, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(konturlar))
#kontuları çizdirmek

cv2.drawContours(goruntu,konturlar,-1,(0,0,255),1)





cv2.imshow("orijinal",goruntu)
# cv2.imshow("gri",gri)
# cv2.imshow("sb",sb)
# cv2.imshow("sba",sba)
cv2.imshow("canny",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()