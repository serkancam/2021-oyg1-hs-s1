import cv2
import numpy as np
import os

yol=os.path.join(os.getcwd(),"images","yuz.jpg")

goruntu=cv2.imread(yol)
bulanik=cv2.blur(goruntu,(15,15))

cv2.imshow("orijinal",goruntu)
cv2.imshow("bulanik",bulanik)
cv2.waitKey(0)
cv2.destroyAllWindows()

