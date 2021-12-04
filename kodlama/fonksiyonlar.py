#1-parametre almayan geriye değer döndürmeyen
def merhaba():    
    for i in range(5):
        print("merhaba")
#2- 1 parametre alıp geriye değer döndürmeyen
def merhaba2(adet):
    for i in range(adet):
        print("Hello")
def topla(s1,s2):
    print(s1+s2)


merhaba()
merhaba2(3)
a=int(input("sayı gir:"))
b=int(input("sayı gir:"))
topla(a,b)

