from collections import deque

def bfs(i,j,k,cost):
    global answer
    q=deque()
    visited=[[0 for _ in range(N)] for _ in range(N)]
    visited[i][j]=1
    q.append((i,j))
    count=0
    while q:
        x,y=q.popleft()
        if arr[x][y]==1:
            count+=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                visited[nx][ny] = visited[x][y]+1
                if visited[nx][ny]<=k:
                    q.append((nx,ny))
    pay = count*M
    if pay>=cost:
        answer = max(answer,count)

T = int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    K = N+1
    answer=0

    for k in range(K,0,-1):
        cost = k*k + (k-1)*(k-1)
        for i in range(N):
            for j in range(N):
                bfs(i,j,k,cost)
        if answer !=0:
            break
    print(f"#{tc+1} {answer}")
