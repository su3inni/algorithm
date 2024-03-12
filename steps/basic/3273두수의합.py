n = int(input())

arr = list(map(int,input().split()))
x = int(input())

arr.sort()
left = 0
right = n-1
answer=0

while left<right:
    if arr[left]+arr[right] == x :
        answer+=1
        left+=1
    elif arr[left]+arr[right] < x :
        left+=1
    else:
        right-=1

print(answer)
