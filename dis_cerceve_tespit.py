import cv2

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    frame=cv2.flip(frame,1)
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    _,sb=cv2.threshold(gri,70,255,cv2.THRESH_BINARY)
    sb_a=cv2.adaptiveThreshold(gri,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,7)
    canny = cv2.Canny(gri,50,240)

    cv2.imshow("renkli",frame)
    cv2.imshow("gri",gri)
    cv2.imshow("sb",sb)
    cv2.imshow("sba",sb_a)
    cv2.imshow("canny",canny)
   
    if cv2.waitKey(1) & 0xFF== ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
