# 3- Parametre alan ve geriye değer döndüren fonskiyon

def fib(adim):
    s1=1
    s2=1
    for i in range(2,adim):
        t=s2
        s2=s1+s2
        s1=t
    return s2

a = int(input("adımı giriniz:"))
print(fib(a))



# #3. adım
# t=s2
# s2=s1+s2
# s1=t
# #4. adım
# t=s2
# s2=s1+s2
# s1=t
# #5. adım
# t=s2
# s2=s1+s2
# s1=t
# #6. adım
# t=s2
# s2=s1+s2
# s1=t
# #7. adım
# t=s2
# s2=s1