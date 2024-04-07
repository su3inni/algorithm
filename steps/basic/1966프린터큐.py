T = int(input())

from collections import deque
for t in range(T):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    weights = sorted(arr,reverse=True)

    q = deque()
    for idx,a in enumerate(arr):
        q.append([a,idx])

    idx = 0
    cnt = 0
    while 1 :
        target = q.popleft()
        if target[0]==weights[idx]:
            cnt += 1
            if target[1]==M:
                print(target)
                print(cnt)
                break
            idx+=1
        else:
            q.append(target)



