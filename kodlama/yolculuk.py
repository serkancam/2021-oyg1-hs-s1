kutupyaricap=6357
ekvatoryaricap=6379
pi=3.14
kutupcevre=2*pi*kutupyaricap
ekvatorcevresi=2*pi*ekvatoryaricap
parkerhiz=150

# parker uzay aracı kutupları ve ekvatoru kaç saniyede dolaşır?
kutup_suresi_sn= kutupcevre/parkerhiz
ekvator_suresi_sn= ekvatorcevresi/parkerhiz
print(f"kutup çevresini {kutup_suresi_sn} saniyede dolaşır.")
print(f"ekvator çevresini {ekvator_suresi_sn} saniyede dolaşır.")
# süreleri dakika-saniye cinsinden dolaşır bulunuz?

kutup_dakika , kutup_saniye = int(kutup_suresi_sn//60), kutup_suresi_sn % 60
print(f"kutup çevresini {kutup_dakika} dakika {kutup_saniye} saniye de dolaşır")



