import cv2
import numpy as np
import os

yol=os.path.join(os.getcwd(),"images","chp2","zebrasmall.png")
goruntu = cv2.imread(yol)

h,w,c = goruntu.shape

angle = 45 #açı
center = (h//2,w//2)#dönme noktası
scale=1.0 # dönme boyutu
carpan=0.98
while True:
    donme_matrisi=cv2.getRotationMatrix2D(center,angle,scale)
    donmus_goruntu=cv2.warpAffine(goruntu,donme_matrisi,(w,h))
    # cv2.imshow("zebra",goruntu)
    cv2.imshow("donmus zebra",donmus_goruntu)
    angle+=10
    if scale < 0.05:
        carpan = 1.02
    elif scale > 1.0:
        carpan = 0.98
    scale *= carpan

    if cv2.waitKey(5) & 0xFF == ord('q'):#cv2.waitKey(5)==27:
        break
cv2.destroyAllWindows()