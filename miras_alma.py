import datetime
class UlasimAraci():
    def __init__(self, marka, yili, hizi, rengi):
        self.marka = marka
        self.yili = yili
        self.hizi = hizi
        self.rengi = rengi
    def yasi_kac(self):
        bu_yil=datetime.date.today().year
        yas=bu_yil-self.yili
        return yas
class Kara(UlasimAraci):
    def __init__(self,marka,yili,hizi,rengi,tekerlek_sayisi,yakit_turu):
        super().__init__(marka,yili,hizi,rengi)
        self.tekerlek_sayisi=tekerlek_sayisi
        self.yakit_turu=yakit_turu
class Hava(UlasimAraci):
    def __init__(self, marka, yili, hizi, rengi,kanat_sayisi,model,motor_turu):
        super().__init__(marka, yili, hizi, rengi)
        self.kanat_sayisi=kanat_sayisi
        self.model=model
        self.motor_turu=motor_turu
class Su(UlasimAraci):
    def __init__(self, marka, yili, hizi, rengi,pervane_sayisi,kamara_sayisi,turu):
        super().__init__(marka, yili, hizi, rengi)
        self.pervane_sayisi=pervane_sayisi
        self.kamara_sayisi=kamara_sayisi
        self.turu=turu    

arac1=UlasimAraci("ford",1986,175,"mavi")
print(arac1.yasi_kac())
ka1=Kara("jeep",2020,190,"pembe",4,"dizel")
print(ka1.yasi_kac())
print(ka1.rengi)

