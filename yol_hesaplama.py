# bir uzay aracının hızını saniye cinsinden km olarka alıp, kutup veya ekvator çevreini kaç saniyede dolaşacağını saniye cinsinden hesaplayıp ekrana yazdıran fonksiyonu yazdırınız.

def zaman_hesapla(hiz):
    kutup_c=3.14*6357**2
    ekvator_c=3.14*6378**2
    kutup_zamani=kutup_c/hiz
    ekvator_zamani=ekvator_c/hiz
    print(f"ekvator çevresini {hiz} km/sn hızla {ekvator_zamani} saniyede dolaşır")
    print(f"kutup çevresini {hiz} km/sn hızla {kutup_zamani} saniyede dolaşır")

zaman_hesapla(300)
zaman_hesapla(952)