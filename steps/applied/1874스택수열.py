K = int(input())

import sys
arr=[]
for k in range(K):
    num = int(sys.stdin.readline())
    arr.append(num)

inputnum = [i+1 for i in range(K)]

stack=[]
numidx=0
arridx=0

answer=[]
while numidx<K:
    target = inputnum[numidx]
    stack.append(target)
    answer.append("+")

    while stack:
        if stack[len(stack)-1] == arr[arridx] :
            stack.pop()
            answer.append("-")
            arridx+=1
        else:
            break
    numidx+=1

if stack:
    for i in range(len(stack)):
        check = stack.pop()
        if check != arr[arridx]:
            answer=["NO"]
            break
        else:
            numidx+=1

for a in answer:
    print(a)
