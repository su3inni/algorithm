from collections import deque
import sys

T = int(input())

for _ in range(T):
    order = sys.stdin.readline()
    n = int(input())
    origin = sys.stdin.readline()
    origin = origin[1:-2]
    origin = origin.split(',')

    arr=deque()
    if n!=0:
        for a in origin :
            arr.append(a)

    errorflag=False
    calcflag=1
    for o in order:
        if o=='R':
            calcflag*=-1
        elif o=='D':
            if len(arr)==0:
                errorflag=True
                break
            else:
                if calcflag==1:
                    arr.popleft()
                else:
                    arr.pop()
    if errorflag:
        print("error")
    else:
        if calcflag==-1:
            arr.reverse()
        result = ",".join(arr)
        print("["+result+"]")
