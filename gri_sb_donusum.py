import cv2
import numpy as np
import os

yol=os.path.join(os.getcwd(),"images","yuz.jpg")

goruntu=cv2.imread(yol)
gri = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)

(t,sb)=cv2.threshold(gri,60,255,cv2.THRESH_BINARY)
(t,sb2)=cv2.threshold(gri,60,255,cv2.THRESH_BINARY_INV)
# print(goruntu.shape)
# print(gri.shape)
print(t)

cv2.imshow("renkli",goruntu)
cv2.imshow("gri",gri)
cv2.imshow("sb",sb)
cv2.imshow("sb2",sb2)
cv2.waitKey(0)
cv2.destroyAllWindows()
