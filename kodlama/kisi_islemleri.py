from kisi import Kisi
while True:
    islem =int( input("bir işlem seçiniz(okuma-0, yazma-1,çıkış-2,yaş ortalaması-3):"))
    if islem==0:
        dosya=open("kisiler.txt","r",encoding="utf-8")
        for satir in dosya:
            print(satir,end="")
        dosya.close()
    elif islem==1:
        while True:
            try:
                ad=input("adınız:")
                soyad=input("soyadınız:")
                if len(ad)<2 or len(soyad)<2:
                    print("ad ve soyad en az 2 karakterli olmalı")
                    continue
                yas=int(input("yaşınız:"))
                break
            except:
                print("hata")
                continue        
        kisi = Kisi(ad,soyad,yas)
        kisi.yaz("kisiler.txt")        
    elif islem==2:
        break
    elif islem==3:
        dosya = open("kisiler.txt","r",encoding="utf-8")
        ortalama=0
        adet=0
        for satir in dosya:
            yas = int(satir.split(",")[2].strip())
            ortalama+=yas
            adet+=1
        ortalama=ortalama/adet
        print(f"Grubun yaş ortalaması={ortalama}")
    else:
        print("hatalı seçim")
