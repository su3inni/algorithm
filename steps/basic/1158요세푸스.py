from collections import deque
N,K = map(int,input().split())

arr = [ i+1 for i in range(N)]
arr = deque(arr)

cnt=0
answer=[]
while arr:
    # 요거 땜시 시간초과일수도..
    # if sum(arr)==0:
    #     break
    target = arr.popleft()
    if cnt==K-1:
        answer.append(target)
        cnt=0
    else:
        arr.append(target)
        cnt+=1

ans=""
for i,a in enumerate(answer):
    if i==0:
        ans+='<'
    ans+=str(a)
    if i!=len(answer)-1:
        ans+=', '
ans+='>'

print(ans)

