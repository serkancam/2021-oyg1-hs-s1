import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    durum,cerceve=cap.read() 
    gri=cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    _,sb=cv2.threshold(gri,60,255,cv2.THRESH_BINARY)
    sbd=cv2.dilate(sb,None,iterations=3)
    sbe=cv2.erode(sb,None,iterations=3)
    
    cv2.imshow("cap",sb)   
    cv2.imshow("sbd",sbd)   
    cv2.imshow("sbe",sbe)   
    if cv2.waitKey(40) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

