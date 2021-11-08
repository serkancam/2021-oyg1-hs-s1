class Araba():
    def __init__(self,renk,marka):
        self.__renk=renk
        self.__marka=marka
        self.__model=1983
        self.__hiz=180
        self.__vites=5
        self.__fiyat=0.0
    def hiz_bilgisi(self):
        return self.__hiz
    def hiz_belirle(self,deger):
        if deger>0 and deger<500:
            self.__hiz=deger
    def model_bilgisi(self):
        return self.__model
    def model_belirler(self,model):
        if model>=1983 and model<=2021:
            self.__model=model
    def vites_bilgisi(self):
        return self.__vites
    def vites_belirle(self,vites):
        if vites>=4 and vites<=7:
            self.__vites=vites
    
        
    

a1=Araba("kırmızı","hyundai")
a2=Araba("mavi","Fiat")
a3=Araba("kırımızı","Ferrari")
a1.hiz_belirle(400)
print(a1.hiz_bilgisi())

     