def yamuk_cevresi(a,b,c,d):
    print("a=",a)
    print("b=",b)
    print("c=",c)
    print("d=",d)
    print(30*"-")
    return a+b+c+d


# pozisyona  dayalı parametre gönderme
c1=yamuk_cevresi(3,4,5,6)
# isme dayalı parametre gönderme
c2=yamuk_cevresi(b=8,a=9,d=7,c=3)

# eğer bir parametre isme dayalı göndrilirse devamıda isme dayalı gönderilmelidir.

# c3=yamuk_cevresi(d=5,3,5,8) hatalı

c4=yamuk_cevresi(3,4,d=5,c=8)