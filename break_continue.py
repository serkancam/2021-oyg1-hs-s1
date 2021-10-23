# bazı durumlarda döngülerimizi bitirmek veya bazı döngü adımlarını atlamak isteyebiliriz.
# bu durumda döngüyü bitirmek için break bir adımı atlamak için continue anahtar kelimeleri
# kullanılır

for i in range(1,16):
    if i%2==0:
        continue # döngünün diğer adımına geçer
    print(i)
print(30*"*")
t=0
while t<12:
    print(t)
    if t==7:
        break # döngüyü bitirir.
    t+=1

for e in range(8):
    for f in range(8):
        if e==5:
            break

