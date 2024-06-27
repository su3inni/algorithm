N , K = map(int,input().split())
vals=[]
for _ in range(N):
    v = int(input())
    vals.append(v)

vals.sort(reverse=True)

price=K
cnt = 0
for v in vals:
    # price>v 수식이 오답의 원인
    if price//v !=0 and price >= v :
        cnt += price//v
        price = price - (price//v)*v

print(cnt)
