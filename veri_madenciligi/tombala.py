# her kartta birbirinde 1-90 arası 15 sayı olan bir liste oluşturunuz
# oyunda 1-90 arası sayıları sizin bir tuşa basmanız ile sırayla 
import random
a=[]
while len(a)<15:
    tut=random.randint(1,90)
    if  a.count(tut)==0:
        a.append(tut)
# a=a.sort()
a.sort()
print(a)