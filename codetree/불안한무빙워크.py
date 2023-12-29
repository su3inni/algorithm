from collections import deque

N,K = map(int,input().split())
safety = list(map(int,input().split()))
people = [0 for i in range(N*2)]

safety = deque(safety)
people = deque(people)

answer=0

while True:
    answer+=1
    print(">>",answer,"번째")

    # 무빙워크 이동
    # 무빙워크 이동하면서 사람도 이동
    safety.rotate(1)
    people.rotate(1)
    # MISSING POINT1. 단, 1~3번 과정 중 N번 칸 위치에 사람이 위치하면 즉시 내립니다.
    if people[N-1]!=0:
        people[N-1]=0

    print("무빙워크 이동")
    print(people)
    print(safety)
    print()

    # MISSING POINT2. 가장 먼저 무빙워크에 올라간 사람부터!!!
    for idx in range(N-1,0,-1):
        print(idx)
        # 사람 이동하고 # 안정성 감소
        if people[idx]==1 :
            if people[idx+1]==0 and safety[idx+1]!=0:
                people[idx]=0
                people[idx+1]=1
                safety[idx+1]-=1
                # CHECK POINT1. 움직이고 안정성 -1 한 후 0이되면 그 무빙워크의 사람은 내리나? > 안내린다

    if people[N-1]!=0:
        people[N-1]=0
    print("사람 이동")
    print(people)
    print(safety)
    print()

    # 사람 추가
    if safety[0]!=0 and people[0]==0:
        people[0]=1
        safety[0]-=1

    print("사람 추가 및 탈락")
    print(people)
    print(safety)
    print()

    count=0
    for i in range(2*N):
        if safety[i]==0:
            count+=1
    print(count,"개")

    if count>=K:
        break

print(answer)


