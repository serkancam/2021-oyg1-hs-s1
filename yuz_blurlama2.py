import cv2
import numpy as np
import os

yol=os.path.join(os.getcwd(),"images","yuz.jpg")

goruntu=cv2.imread(yol)

parca=goruntu[170:440,170:380]
parca=cv2.blur(parca,(35,35))
goruntu[170:440,170:380]=parca

cv2.imshow("orijinal",goruntu)
# cv2.imshow("bulanik",bulanik)
cv2.waitKey(0)
cv2.destroyAllWindows()
