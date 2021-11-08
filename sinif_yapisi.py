# bir fonksiyon sınıf içinde tanımlanırsa method adını alır.
# self anahtar kelimesi sınftan türetilen nesnelerin özelliklerini işaret etmek için kullanılır.
# bir method nesneye ait özellikleri kullanmak için parametre olarak self değerini almalıdır.
class Insan():
    def __init__(self):#yapıcı 
        self.ad=""
        self.cinsiyet=""
        self.boy=0.0
        self.yas=0
        self.kilo=0.0
        self.sac_rengi="sarı"
        print("yapıcı çalıştı")
    def boy_arttir(self,deger):
        self.boy=round(self.boy+deger,2)

class Hayvan():
    def __init__(self) :
        self.boy=0.0
        self.kilo=0.0
        self.tur=""
    def yemek_ye(self,miktar):
        self.kilo+=miktar

h1=Hayvan()
h2=Hayvan()   
h3=Hayvan()   
h4=Hayvan()   

ali=Insan()
ayse=Insan()
ali.ad="ali"
ayse.ad="ayşe"
ayse.ad="boş"
print(ali.ad)
print(ayse.ad)
# print(Insan.ad)
ali.boy=1.58
ali.boy_arttir(0.3)
print(ali.boy)
