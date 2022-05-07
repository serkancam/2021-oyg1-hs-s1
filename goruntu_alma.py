import cv2
import numpy as np
import os
cd =os.getcwd()#os.getcwd() bize şu anda çalşan python dosyasının bulunduğu dizin bilgisini verir cd--> current directory
print(cd) 
#resim yolunu (path) oluşturalım adına img_path diyelim
img_path = os.path.join(cd,"images","chp1","marsrover.png")
#marsrover.png resminin verisini img adında bir değişken aktaralım
# burada opencv görüntü verilerini numpy dizisi şeklinde alır
img = cv2.imread(img_path)
#resim bilgileri
print("resim verisi kaç boyutlu",img.ndim)
print("resim boyutlarını şekli",img.shape)
print("resim yukseklik",img.shape[0])
print("resim genişlik",img.shape[1])
print("resim renk kanal sayısı",img.shape[2])
#resmi gösterelim
#resmin bir parçasını alalım
img1=img[0:200,0:320]
img2=img[0:200,320:]
img3=img[200:,0:320]
img4=img[200:,320:]
img[350:,620:]=(0,255,0)
# resme içi boş bir dörtgen ekleyelim
baslangic=(100,70)
bitis=(350,380)
renk=(255,0,0)
cv2.rectangle(img,baslangic,bitis,renk,4)
# circle
cv2.circle(img,baslangic,30,renk,3)
cv2.circle(img,(100,380),30,(255,0,0),3)
cv2.circle(img,(350,70),30,(255,0,0),3)
cv2.circle(img,bitis,30,(255,0,0),3)
cv2.imshow("marsrover",img)
cv2.imshow("marsrover1",img1)
cv2.imshow("marsrover2",img2)
cv2.imshow("marsrover3",img3)
cv2.imshow("marsrover4",img4)

cv2.waitKey(0)
cv2.destroyAllWindows()
print("Çıkış")
dosya_yolu=os.path.join(cd,"images","chp1","marsrover_degisen.jpg")
cv2.imwrite(dosya_yolu,img)

