T = int(input())

def calc(time,stair_length):
    #d_count 대기인원
    count,d_count=0,0
    ing_queue=[]

    while time or ing_queue or d_count:
        # 대기하는 사람이 있는 경우
        while d_count:
            # 계단을 내려가는 중인 사람
            if len(ing_queue)==3:
                break
            ing_queue.append(stair_length)
            d_count-=1

        # 내려가는 사람이 있을 때
        for i in range(len(ing_queue)-1,-1,-1):
            ing_queue[i]-=1
            if ing_queue[i]<=0:
                ing_queue.pop(i)

        # 계단까지 이동중인 사람이 있다면
        for i in range(len(time)-1,-1,-1):
            time[i]-=1
            #계단까지 다 갔다면
            if time[i]<=0:
                time.pop(i)
                d_count+=1
        count+=1
    return count

# 어떤 계단을 이용할지 조합 찾기
def comb(idx):
    global min_count
    if idx==len(person):
        stair_list1, stair_list2=[],[]
        # 1번 2번 계단 분리해서 넣기
        for i in range(len(person)):
            if person_stair_use[i]==0:
                stair_list1.append(person_distance[i][0])
            else:
                stair_list2.append(person_distance[i][1])
        stair_list1=sorted(stair_list1)
        stair_list2=sorted(stair_list2)

        count = max(calc(stair_list1,stairs[0][2]),calc(stair_list2,stairs[1][2]))
        min_count=min(count,min_count)
        return

    person_stair_use[idx]=0
    comb(idx+1)
    person_stair_use[idx]=1
    comb(idx+1)



for tc in range(T):
    N = int(input())
    arr = [ list(map(int,input().split())) for _ in range(N)]

    person=[]
    stairs=[]

    # 사람과 계단의 위치 파악
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                person.append((i,j))
            elif arr[i][j] > 1 :
                #계단 길이도 추가해야함
                stairs.append((i,j,arr[i][j]))

    # 각 사람마다 계단 1, 계단 2까지의 거리
    person_distance=[]
    for i in range(len(person)):
        s1_d = abs(person[i][0]-stairs[0][0])+abs(person[i][1]-stairs[0][1])
        s2_d = abs(person[i][0]-stairs[1][0])+abs(person[i][1]-stairs[1][1])
        person_distance.append((s1_d,s2_d))

    # 0이면 1번 stair, 1이면 2번 stair
    person_stair_use = [0 for _ in range(len(person))]
    min_count = 99999999

    comb(0)

    print(f"#{tc+1} {min_count + 1}")
