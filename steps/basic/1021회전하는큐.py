N,M = map(int,input().split())
pops = list(map(int,input().split()))

from collections import deque
bdq = deque([i+1 for i in range(N)])

answer=0
for target in pops:
    while 1:
        tidx = bdq.index(target)
        if tidx==0:
            bdq.popleft()
            break
        elif tidx <= len(bdq)//2:
            mv = bdq.popleft()
            bdq.append(mv)
            answer+=1
        else:
            mv = bdq.pop()
            bdq.appendleft(mv)
            answer+=1

print(answer)
