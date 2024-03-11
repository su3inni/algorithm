nanjang = []
for _ in range(9):
    n = int(input())
    nanjang.append(n)

total = sum(nanjang)
d1=0
d2=0
for i in range(9):
    for j in range(i+1,9):
        if total - nanjang[i] - nanjang[j] == 100 :
            d1=nanjang[i]
            d2=nanjang[j]


nanjang.remove(d1)
nanjang.remove(d2)
nanjang.sort()
for n in nanjang:
    print(n)
