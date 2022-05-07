import cv2
import numpy as np
import os

yol1=os.path.join(os.getcwd(),"images","chp2","nature.jpg")

goruntu=cv2.imread(yol1)

parca=goruntu[60:150,300:400]#satir aralğı,sütun aralığı

gri=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
(T,sb)=cv2.threshold(gri,60,255,cv2.THRESH_BINARY)



cv2.imshow("gri",gri)
cv2.imshow("sb",sb)
cv2.imshow("orijinal",goruntu)
cv2.imshow("parca",parca)
cv2.waitKey(0)
cv2.destroyAllWindows()