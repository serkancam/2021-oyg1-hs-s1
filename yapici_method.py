class Personel():
    def __init__(self,ad1:str=" ",soyad1:str="",yas1:int=0,gorev1:str="",maas1:float=0.0):
        self.ad=ad1
        self.soyad=soyad1
        self.yas=int(yas1)
        self.gorev=gorev1
        self.maas=float(maas1)
    #  bu sınıfta maasa belirtilen değer kadar zam yapan bir metod yazınız(zam_yap)
    #  bu sınıfa aldığı parametre ile kişinin görev türünü değitiren bir metod yazınız(gorev_degistir)
    def zam_yap(self,deger):
        self.maas+=deger
    def gorev_degistir(self,gorev):
        self.gorev=gorev


serkan=Personel("serkan","çam",39,"öğretmen",6000)
balkan=Personel()
balkan.ad="balkan"
balkan.soyad="mesut"
balkan.gorev="öğrenci"
balkan.maas=10

print(balkan.maas)
print(serkan.maas)
