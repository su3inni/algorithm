N,M = input().split()
N,M = int(N),int(M)


answer=[]
def recur(path):
    if len(path)==M:
        answer.append(path)
        return

    for i in range(1,N+1):
        # 중복 없이
        if str(i) not in path :
            if len(path)==0:
                last_int=0
            else:
                last_int = int(path[len(path)-1])
            if i > last_int:
                recur(path+str(i))

recur('')
answer.sort()

for a in answer:
    for i in range(len(a)):
        print(a[i],end=" ")
    print()