import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ret1,frame1=cap.read()
ret2,frame2=cap.read()

while True:
    fark = cv2.absdiff(frame1,frame2)
    gri=cv2.cvtColor(fark,cv2.COLOR_BGR2GRAY)
    yumusak=cv2.GaussianBlur(gri,(3,3),0)
    t,sb=cv2.threshold(yumusak,20,255,cv2.THRESH_BINARY)
    yayilmis=cv2.dilate(sb,None,iterations=3) 
    konturlar,_=cv2.findContours(yayilmis,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for kontur in konturlar:
        (x,y,w,h)=cv2.boundingRect(kontur)
        if cv2.contourArea(kontur)<4000:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.putText(frame1,"hareket algilandi",(10,30),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),1)

    
    cv2.imshow("sonuc",frame1)
    frame1=frame2
    ret2,frame2=cap.read()
    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()
