import cv2
import numpy as np

cap = cv2.VideoCapture(0)

_,feski=cap.read()
_,fyeni=cap.read()
while True:
    fark = cv2.absdiff(feski,fyeni)
    f1=feski.copy()
    f2=feski.copy()
    gri=cv2.cvtColor(fark,cv2.COLOR_BGR2GRAY)
    bulanik=cv2.GaussianBlur(gri,(3,3),0)
    t,sb=cv2.threshold(bulanik,60,255,cv2.THRESH_BINARY)
    sb=cv2.dilate(sb,None,iterations=3)
    # 1. yol
    if np.count_nonzero(sb)>1000:
        cv2.putText(f1,"hareket algilandi",(10,50),cv2.FONT_HERSHEY_SIMPLEX,2.0,(0,255,0),2)
    # 2. yol
    konturlar,_=cv2.findContours(sb,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for kontur in konturlar:
        (x,y,w,h)=cv2.boundingRect(kontur)
        if cv2.contourArea(kontur)<1000:
            continue
        cv2.rectangle(f2,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(f2,"hareket algilandi",(10,50),cv2.FONT_HERSHEY_SIMPLEX,2.0,(0,255,0),2)
    #2. yol bitiş
    cv2.imshow("sonuc",f1)
    cv2.imshow("sonuc2",f2)
    feski=fyeni
    _,fyeni=cap.read()
    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()
