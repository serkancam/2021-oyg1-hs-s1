print("size sorulan her belirti için aşğaıdaki puanlamayı esas alınız.  ")
print("0-hiç 1-nadiren 2-bazen 4-sık sık 8-şiddetli")
ates=int(input("ateş:"))
yorgunluk=int(input("Yorgunluk"))
kuru_oksuruk=int(input("Kuru öksürük"))
solunum_zorlugu=int(input("solunum zorluğu"))
oksuruk=int(input("Öksrük"))
agri=int(input("Ağrı"))
toplam=ates+yorgunluk+kuru_oksuruk+solunum_zorlugu+oksuruk+agri

if toplam>27:
    print("covid belirtileri var")
elif toplam>17 and toplam<28:
    print("Grip belirtileriniz var.")
elif toplam>3 and toplam<18:
    print("nezle belirtileriniz var.")
else:
    print("Bir hastalık belirtiniz yok.")
