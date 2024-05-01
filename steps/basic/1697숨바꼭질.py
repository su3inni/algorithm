N,K = map(int,input().split())

mincnt = 10**5

from collections import deque
def move(N):
    global mincnt
    q = deque()
    q.append((N,0))
    hist = set()
    hist.add(N)
    while q:
        num,cnt = q.popleft()
        if num==K :
            if cnt<mincnt:
                mincnt = cnt
            break
        
        # new 값의 범위가 0<= <= 100,000 조건을 넣어주고 나니 메모리초과 해결됨.. 
        # new 값 자체의 범위가 너무 작아지거나 너무 커지지 않도록 주의해야함
        new = num+1
        if new not in hist and 0<=new<=100000:
            q.append((new,cnt+1))
            hist.add(new)

        new = num*2
        if new not in hist and 0<=new<=100000:
            q.append((new,cnt+1))
            hist.add(new)

        new = num-1
        if new not in hist and 0<=new<=100000:
            q.append((new,cnt+1))
            hist.add(new)



move(N)
print(mincnt)
