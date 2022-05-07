import cv2 
import os
import numpy as np

yol=os.path.join(os.getcwd(),"images","chp2","scanned_doc.png")
g=cv2.imread(yol)
g=cv2.cvtColor(g,cv2.COLOR_BGR2GRAY)
(t,sb)=cv2.threshold(g,60,255,cv2.THRESH_BINARY)

sbd=cv2.erode(sb,None,iterations=1)

cv2.imshow("sb",sb)
cv2.imshow("sbd",sbd)
cv2.waitKey(0)
cv2.destroyAllWindows()
