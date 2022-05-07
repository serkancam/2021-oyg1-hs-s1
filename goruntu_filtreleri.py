import cv2
import numpy as np
import os

yol1=os.path.join(os.getcwd(),"images","chp2","nature.jpg")
yol2=os.path.join(os.getcwd(),"images","chp2","salt-pepper.jpg")
doga=cv2.imread(yol1)
beyin=cv2.imread(yol2)

#filtreler
# mean(ortalama),median(ortanca),gaussian
#filtrlerde çekirdek(kernel) işlemi yapılır
#meanfilter
doga_mf1=cv2.blur(doga,(3,3))
doga_mf2=cv2.blur(doga,(13,13))
beyin_mf1=cv2.blur(beyin,(5,5))
#median filter
doga_md1=cv2.medianBlur(doga,13)
beyin_md1=cv2.medianBlur(beyin,5)
#gösterimler
cv2.imshow("beyin",beyin)
cv2.imshow("beyin mf1",beyin_mf1)
cv2.imshow("beyin md1",beyin_md1)
# cv2.imshow("doga",doga)
# cv2.imshow("doga mf1",doga_mf1)
# cv2.imshow("doga mf2",doga_mf2)
# cv2.imshow("doga md1",doga_md1)

cv2.waitKey(0)
cv2.destroyAllWindows()