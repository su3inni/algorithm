num = input()

cnt = [0 for _ in range(10)]

for n in num:
    idx = int(n)
    cnt[idx]+=1


maxcnt=0
for c in range(len(cnt)):
    if c !=6 and c!=9:
        maxcnt = max(maxcnt,cnt[c])

if (cnt[6]+cnt[9])%2==0:
    cpcnt = (cnt[6]+cnt[9])//2
else:
    cpcnt = (cnt[6]+cnt[9])//2+1

answer = max(maxcnt,cpcnt)
print(answer)
