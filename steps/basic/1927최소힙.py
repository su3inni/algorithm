N = int(input())
import sys
import heapq
arr=[]
for _ in range(N):
    n = int(sys.stdin.readline())
    if n==0 :
        if len(arr)!=0 :
            target = heapq.heappop(arr)
            print(target)
        else:
            print(0)
    else:
        heapq.heappush(arr,n)
