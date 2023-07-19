N,M = input().split(' ')
N,M =int(N),int(M)
answer=[]
def recur(arr):
   if len(arr)==M:
       answer.append(arr)
       return
   for i in range(1,N+1):
        if str(i) not in arr:
            recur(arr+str(i))


recur('')
answer.sort()
for a in answer:
    for i in range(len(a)):
        print(a[i],end=' ')
    print()