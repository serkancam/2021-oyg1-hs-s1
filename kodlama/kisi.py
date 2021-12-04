class Kisi():
    def __init__(self,ad,soyad,yas):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
    def yaz(self,dosya_yolu):
        satir=self.ad+","+self.soyad+","+str(self.yas)+"\n"
        dosya=open(dosya_yolu,"a",encoding="utf-8")
        dosya.write(satir)
        dosya.close()