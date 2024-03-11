a,b = map(int,input().split())

if a==b:
    print(0)
else:
    answer=[]
    if a<b:
        for i in range(a+1,b):
            answer.append(i)
    else:
        for i in range(b+1,a):
            answer.append(i)

    print(len(answer))
    for a in answer:
        print(a,end=' ')
