# kullanıcının giridiği sayıyı kalansız bölen sayıları ekrana yazıdırınız
# 15-->1 3  5 15
# 50 --> 1 2 5 10 25 50
# 7 --> 1 7
# 13 --> 1 13

sayi = int(input("Bölenleri bulunacak sayıyı giriniz:"))

for i in range(1,sayi+1):
    if sayi % i == 0:
        print(i)

