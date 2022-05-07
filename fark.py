import cv2

r1=cv2.imread("/home/serkan/Belgeler/2021-oyg1-hs-s1/images/r1.png")
r2=cv2.imread("/home/serkan/Belgeler/2021-oyg1-hs-s1/images/r2.png")

r1=cv2.resize(r1,(513,325),interpolation=cv2.INTER_AREA)
r2=cv2.resize(r2,(513,325),interpolation=cv2.INTER_AREA)
fark=cv2.absdiff(r1,r2)
fark=cv2.cvtColor(fark,cv2.COLOR_BGR2GRAY)

t,sb=cv2.threshold(fark,50,255,cv2.THRESH_BINARY_INV)

cv2.imshow("fark",fark)
cv2.imshow("fark",sb)
cv2.waitKey(0)