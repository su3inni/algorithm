card = [ i+1 for i in range(20)]
for t in range(10):
    a,b = map(int,input().split())
    a-=1
    section = card[a:b]
    section = section[::-1]
    for i in range(a,b):
        card[i] = section[i-a]

for c in card:
    print(c,end=' ')
