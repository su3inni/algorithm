T = int(input())
# 우상 우하 좌하 좌상
dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]

def checkrange(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

def dfs(x, y, d, cnt):
    global si, sj, dessert, max_dessert
    # 종료조건
    # 원점으로 돌아오고 사각형 만들었을 때
    if x == si and y == sj and cnt == 4:
        max_dessert = max(max_dessert, len(dessert))
        return

    for i in range(2):
        nd = (d + i) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if checkrange(nx, ny) and arr[nx][ny] not in dessert:
            dessert.append(arr[nx][ny])
            cnt += i
            dfs(nx, ny, nd, cnt)
            idx = dessert.index(arr[nx][ny])
            dessert.pop(idx)


for tc in range(T):
    N= int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_dessert=-1
    for si in range(N):
        for sj in range(N):
            cnt=1
            dessert=[]
            dfs(si,sj,1,cnt)
            # print(dessert)

    print(f"#{tc+1} {max_dessert}")
