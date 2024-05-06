from collections import deque

R,C,T = map(int,input().split())

arr = []
aircleaner = []
munzi = deque()
for i in range(R):
    rw = list(map(int,input().split()))
    for j in range(C):
        if rw[j]==-1:
            aircleaner.append(i)
        elif rw[j]!=0:
            munzi.append((i,j))
    arr.append(rw)

aircleaner.sort()

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def spread(arr,munzi):
    add_munzi = [ [ 0 for _ in range(C)] for _ in range(R)]

    while munzi:
        r,c = munzi.popleft()
        cnt=0
        spm = arr[r][c]//5

        for d in range(4):
            nr = r + dx[d]
            nc = c + dy[d]
            if 0<=nr<R and 0<=nc<C :
                if nr in aircleaner and nc==0:
                    continue
                else:
                    cnt+=1
                    add_munzi[nr][nc] += spm

        add_munzi[r][c] -= spm*cnt


    new_arr = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            new_arr[i][j] = add_munzi[i][j]+arr[i][j]

    return new_arr

def rotate(arr):
    rarr = [[0 for _ in range(C)] for _ in range(R)]

    # 반시계방향
    ai,aj = aircleaner[0],0
    si,sj = 0,0
    # 하향
    for i in range(si+1,ai) :
        rarr[i][0] = arr[i-1][0]
    # 하단 : 우향
    for i in range(C-1):
        if arr[ai][i]>0:
            rarr[ai][i+1] = arr[ai][i]
    # 상향
    for i in range(si,ai):
        rarr[i][C-1] = arr[i+1][C-1]
    # 상단 : 좌향
    for i in range(C-1):
        rarr[0][i] = arr[0][i+1]

    # print("공기청정기 상단 회전")
    # for r in rarr:
    #     print(r)

    # 시계방향
    ai,aj = aircleaner[1],0
    si,sj = ai,aj
    # 하향
    for i in range(si+1,R) :
        rarr[i][C-1] = arr[i-1][C-1]

    # 하단 : 우향
    for i in range(C):
        if arr[ai][i-1]>0:
            rarr[ai][i] = arr[ai][i-1]

    # 상향
    for i in range(si,R-1):
        rarr[i][0] = arr[i+1][0]

    # 상단 : 좌향
    for i in range(C-1):
        rarr[R-1][i] = arr[R-1][i+1]

    for i in range(R):
        if i==0 or i==R-1 or i in aircleaner :
            for j in range(C):
                arr[i][j] = rarr[i][j]
        else:
            arr[i][0] = rarr[i][0]
            arr[i][C-1] = rarr[i][C-1]

    for i in aircleaner:
        arr[i][0]=-1

for _ in range(T):
    # 미세먼지 확산
    arr = spread(arr,munzi)

    # 공기청정기
    rotate(arr)
    
    # 이 부분때문에 문제였음 
    # 회전시, 영향받는 요소가 무엇인지 생각하기
    munzi = deque()
    for i in range(R):
        for j in range(C):
            if arr[i][j]>0:
                munzi.append((i,j))


answer=0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0 :
            answer+=arr[i][j]

print(answer)
