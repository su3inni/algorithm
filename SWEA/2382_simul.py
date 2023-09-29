T=int(input())

# 상하좌우
dx=[0,-1,1,0,0]
dy=[0,0,0,-1,1]
opp = {1:2,2:1,3:4,4:3}

def check(time):
    global bio_list
    cnt=0
    while 0<time :
        # 각 칸에 몇 개의 종류가 있는지 기록하는
        ck={}
        for i in range(len(bio_list)):
            nx = bio_list[i][0] + dx[bio_list[i][3]]
            ny = bio_list[i][1] + dy[bio_list[i][3]]
            if (nx,ny) in ck :
                ck[(nx,ny)].append(i)
            else:
                ck[(nx,ny)]=[i]
            bio_list[i][0]=nx
            bio_list[i][1]=ny

        # nx,ny가 가장 자리 범위인지 확인하기
        for i in range(len(bio_list)):
            x,y=bio_list[i][0],bio_list[i][1]
            hm = bio_list[i][2]
            dr = bio_list[i][3]
            # 가장자리인 경우
            if ( x==0 or x==N-1 ) or (y==0 or y==N-1):
                nhm = hm//2
                ndr = opp[dr]
                bio_list[i][2]=nhm
                bio_list[i][3]=ndr

        # 변경된 위치에서 겹치는지 확인하기
        for el in ck:
            if len(ck[el])>=2:
                sum=0
                max_bio=0
                max_idx=0
                for i in ck[el]:
                    sum+=bio_list[i][2]
                    if bio_list[i][2] > max_bio:
                        max_bio=bio_list[i][2]
                        max_idx=i
                    bio_list[i][2]=0
                bio_list[max_idx][2]=sum
                bio_list[max_idx][3]=bio_list[max_idx][3]

        # 미생물 수 0인 군집 삭제하기
        rebio=[]
        for i in range(len(bio_list)):
            if bio_list[i][2]!=0:
                rebio.append(bio_list[i])
        bio_list=rebio

        time-=1

    for bio in bio_list:
        cnt+=bio[2]
    return cnt

for tc in range(T):
    N,M,K = map(int,input().split())
    bio_list=[list(map(int,input().split())) for _ in range(K)]
    ans=check(M)
    print(f"#{tc+1} {ans}")
