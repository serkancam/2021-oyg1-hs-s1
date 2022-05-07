import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    durum,cerceve=cap.read()
    flip1=cv2.flip(cerceve,1)#0,1,-1
    flip0=cv2.flip(cerceve,0)
    
    cv2.imshow("cap",cerceve)
    cv2.imshow("flip1",flip1)
    cv2.imshow("flip0",flip0)

    if cv2.waitKey(40) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

