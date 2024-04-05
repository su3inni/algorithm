N,M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append( list(map(int,input().split())) )

from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j,visited):
    q = deque()
    target_color = arr[i][j]
    q.append([i,j])
    visited[i][j]=1
    total = 1
    rainbow = 0
    # 이 부분 때문에 틀렸었음
    history = []
    while q:
        si,sj = q.popleft()
        for d in range(4):
            nsi = si + dx[d]
            nsj = sj + dy[d]
            # [1-3] 검은 블록은 포함되면 안된다
            if 0<=nsi<N and 0<=nsj<N and arr[nsi][nsj]>=0 and visited[nsi][nsj]==0:
                if 0==arr[nsi][nsj]:
                    rainbow+=1
                    total+=1
                    visited[nsi][nsj]=1
                    q.append([nsi,nsj])
                    history.append([nsi,nsj])
                # [1-4] 일반 블록 색은 모두 같아야한다
                elif arr[nsi][nsj]==target_color:
                    total +=1
                    q.append([nsi,nsj])
                    visited[nsi][nsj]=1
    # 무지개 블럭에 대한 방문처리 원상복구 시켜야함
    for i,j in history:
        visited[i][j]=0
    return total,rainbow


def find_group():
    block_group=[]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j]>=1 and visited[i][j]==0:
                # [1-1] 무지개 블록이 아닌 기준 블록
                total,rainbow = bfs(i,j,visited)
                # [1-2] 블록의 개수가 2보다 크거나 같아야
                if total>=2:
                    block_group.append([i,j,rainbow,total])
    return block_group

def remove(i,j):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    target_color = arr[i][j]
    q = deque()
    q.append([i,j])

    while q:
        si,sj = q.popleft()
        arr[si][sj]= -10
        for d in range(4):
            nsi = si + dx[d]
            nsj = sj + dy[d]
            if 0<=nsi<N and 0<=nsj<N and visited[nsi][nsj]==0:
                if arr[nsi][nsj]==0:
                    q.append([nsi,nsj])
                    visited[nsi][nsj]=1
                elif arr[nsi][nsj]==target_color:
                    q.append([nsi,nsj])
                    visited[nsi][nsj]=1

    return

def fall(arr):
    for r in range(N-1):
        for c in range(N):
            cr,cc = r,c
            while arr[cr][cc]>=0 and arr[cr+1][cc]==-10 and 0<=cr<N-1:
                arr[cr][cc],arr[cr+1][cc] = arr[cr+1][cc],arr[cr][cc]
                cr-=1
    return arr

def rotate(arr):
    tmp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j]= arr[N-j-1][i]
    return tmp
turn=0
score = 0
while 1:
    # [1] 블록 그룹 탐색
    block_group = find_group()
    if len(block_group)==0:
        break
    # [1] 블록 그룹 선택 : 크기가 큰거, 무지개 블록 수가 많은거, 기준 블록의 행이 큰거, 열이 큰거
    block_group.sort(key=lambda x:(x[3],x[2],x[0],x[1]),reverse=True)
    sr,sc,rb,tb = block_group[0][0],block_group[0][1],block_group[0][2],block_group[0][3]
    score+=tb**2

    # [2] 블록 삭제
    remove(sr,sc)
    # [3] 중력
    arr = fall(arr)
    # [4] 회전
    arr = rotate(arr)
    arr = rotate(arr)
    arr = rotate(arr)
    # [5] 중력
    arr = fall(arr)

    turn+=1

print(score)
