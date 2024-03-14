N = int(input())
import sys
arr = list(map(int,sys.stdin.readline().split()))
answer=[0 for _ in range(N)]

stack=[]
for idx,n in enumerate(arr):

    if idx==0:
        stack.append([idx,n])
    else:
        # stack에서 반복돌아야하는 부분
        while stack and stack[-1][1] < n :
            stack.pop()
        if stack:
            ans=stack[-1][0]
            answer[idx] = ans+1
        stack.append([idx,n])

for a in answer:
    print(a,end=' ')


# 완전탐색 시간초과
# copyarr=arr[:]
# while arr:
#     idx = len(arr)-1
#     cmax = arr.pop()
#     rp = len(arr)
#     for i in range(rp,-1,-1):
#         if copyarr[i]>cmax:
#             answer[idx]=i+1
#             break
#
# for a in answer:
#     print(a,end=' ')
