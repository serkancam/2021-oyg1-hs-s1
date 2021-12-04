# bir cümledeki hece sayısı sesli harf sayısına eşittir.

sesli="euüıoiaöEIOUÜİAÖ"#karakter dizisi
#in anahtar kelimesi for döngüsünde içinde dönülecek değerlere işaret eder.
# başka bir kullanımda bir değerin diğer bir listede olup olmadığına bakar. 
# Sonuç True ve False döner

# print("a" in "ali")
# print("A" in "ali")
metin="merhaba dünya."# karakter dizisi
hece_sayisi=0
for harf in metin:
    # print(harf in sesli)
    if harf in sesli:
        hece_sayisi+=1
print(hece_sayisi)