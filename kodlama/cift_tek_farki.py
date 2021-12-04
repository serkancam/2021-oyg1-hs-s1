# kullanıcının girdiği iki sayı arasındaki çift sayılar toplamından tek sayılar toplamını çıkartarak
# sonucu ekrana yazdırınız.

#ilk sayı= 2 
#ikinci sayı =7
# (2+4+6)-(3+5+7)=-3
s1=int(input("1. sayıyı giriniz:"))
s2=int(input("2. sayıyı giriniz:"))
cift=0
tek=0
degisim=1
if s2<s1:
    degisim=-1

for i in range(s1,s2+degisim,degisim):
    if i%2==0:
        cift+=i
    else:
        tek+=i

print(cift-tek)


# if s1<s2:
#     for i in range(s1,s2+1):
#         if i%2==0:
#             cift+=i 
#         else:
#             tek+=i
# else:
#     for i in range(s2,s1+1):
#         if i%2==0:
#             cift+=i #cift=cift+i
#         else:
#             tek+=i