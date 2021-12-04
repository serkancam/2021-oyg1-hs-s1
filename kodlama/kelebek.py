adet=int(input("sayı giriniz:"))
i=1
# while i<=adet:
#     for t in range(i):
#         print( "*",end="")
#     print()
#     i+=1 

while i<=adet:
    print(i*"*",end="")
    print((adet*2-i*2)*" ",end="")
    print(i*"*")
    i+=1
# i=adet-1
# while i>=1:
#     print(i*"*",end="")
#     print((adet*2-i*2)*" ",end="")
#     print(i*"*")
#     i-=1
