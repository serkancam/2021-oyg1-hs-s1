import sqlite3 as sql

okul_no=int(input("okul no:"))
ad=input("ad:")
soyad=input("soyad:")
sinif=int(input("sınıf:"))
sube=input("şube:")

sorgu1 = f"insert into ogrenci values({okul_no},'{ad}','{soyad}',{sinif},'{sube}')"
sorgu2 = "insert into ogrenci values(?,?,?,?,?)"
degerler=[okul_no,ad,soyad,sinif,sube]
print(sorgu2)
vt = sql.connect("/home/serkan/Belgeler/2021-oyg1-hs-s1/veritabani/ogrenciler")
imlec = vt.cursor()
imlec.execute(sorgu2,degerler)
vt.commit()
vt.close()
