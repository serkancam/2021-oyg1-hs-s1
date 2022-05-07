#goruntu_kaydetme.py
import cv2
import os
import numpy as np

resim = np.zeros((400,400,3),dtype=np.uint8)
# tam resmin ortasına yarıçapı 30 olan kırmızı ve kalınlığı 4 olan bir çember çiziniz.
# kırmızı çemberi tam olarak içine alan mavi bir kare çiziniz.
h=resim.shape[0]
w=resim.shape[1]

cv2.circle(resim,(199,199),30,(0,0,255),4)
cv2.rectangle(resim,(167,167),(231,231),(255,0,0),4)


cv2.imshow("resim",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
# oluşan resmin chp1 içine calisma1.jpg olarak kaydedin.
dosya_yolu = os.path.join(os.getcwd(),"images","chp1","calisma1.jpg")
cv2.imwrite(dosya_yolu,resim)