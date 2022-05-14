import cv2
import numpy as np
import os

yol1 = os.path.join(os.getcwd(), "images", "chp2", "sekil_geo.jpg")
yol2 = os.path.join(os.getcwd(), "images", "chp2", "rice_1.jpg")
yol3 = os.path.join(os.getcwd(), "images", "chp2", "elmalar3.jpg")

sekiller = cv2.imread(yol2)
pirincler = cv2.imread(yol2)
elmalar = cv2.imread(yol3)
# gri/blur/canny 
sekiller_gri = cv2.cvtColor(sekiller, cv2.COLOR_BGR2GRAY)
sekiller_blur = cv2.GaussianBlur(sekiller_gri, (3, 3), 0)
sekiller_canny = cv2.Canny(sekiller_blur, 40, 180)
# konturları bul
konturlar_sekil, _ = cv2.findContours(sekiller_canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(konturlar_sekil))
# konturları çizdir
cv2.drawContours(sekiller, konturlar_sekil, -1, (0, 255, 0), 1)

cv2.imshow("sekiller", sekiller)

cv2.waitKey(0)
cv2.destroyAllWindows()
