##################### 다시 한 번 꼭 풀어보기 #######################
N,M,K = map(int,input().split())

maze = [ list(map(int,input().split())) for _ in range(N)]

players={}
for i in range(M):
    a,b = map(int,input().split())
    try:
        players[(a-1,b-1)].append(i)
    except:
        players[(a-1,b-1)]=[i]


exit_x, exit_y = map(int,input().split())
exit_x-=1
exit_y-=1

from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    points = deque()
    distance_board=[[0 for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    points.append([x,y])
    visited[x][y]=1
    while True :
        if len(points)==0:
            return distance_board
        x,y = points.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                distance_board[nx][ny]= distance_board[x][y]+1
                points.append([nx,ny])
                visited[nx][ny]=1
    return distance_board

def move_players():
    update_players={}
    mved=0
    for p in players:
        min_d = 1000
        x, y = p[0], p[1]
        hmp = len(players[p])
        # 최단거리 방향 찾고
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<N :
                if min_d > distance_board[nx][ny] :
                    min_d = distance_board[nx][ny]
        
        # CHECK_POINT. 움직일 수 있는 최단 거리가 한개가 아닐 수도 있음을 생각 못했음
        can_move=[]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<N and distance_board[nx][ny]==min_d:
                can_move.append([nx,ny])
                mx,my = nx,ny

        if len(can_move)>1:
            moved=False
            for mx,my in can_move:
                # 출구라면 탈출
                if [mx,my]==[exit_x,exit_y]:
                    mved+=hmp
                    moved=True
                    break
                # 벽이 아니라면 이동
                if maze[mx][my]==0:
                    # CHECK POINT. 움직이려는 공간에 다른 플레이어가 있을 수 있음을 생각못했음
                    try:
                        pls = players[p]
                        for pp in pls:
                            update_players[(mx,my)].append(pp)
                    except:
                        update_players[(mx,my)] = players[p]
                    mved+=hmp
                    moved=True
                    break

            if moved==False:
                try:
                    pls = players[p]
                    for pp in pls:
                        update_players[(x,y)].append(pp)
                except:
                    update_players[(x, y)]=players[p]

        else:
            if [mx, my] == [exit_x, exit_y]:
                mved+=hmp
            # 벽이 아니라면 이동
            elif maze[mx][my] == 0:
                try:
                    pls = players[p]
                    for pp in pls:
                        update_players[(mx, my)].append(pp)
                except:
                    update_players[(mx, my)] = players[p]
                mved+=hmp
            else:
                try:
                    pls = players[p]
                    for pp in pls:
                        update_players[(x, y)].append(pp)
                except:
                    update_players[(x, y)] = players[p]


    return update_players,mved

def find_spot():
    spot_candi=[]
    for p in players:
        x,y = p[0], p[1]
        # REMIND POINT. 가장 작은 정사각형 구하는거에서 막혔었음
        if x==exit_x:
            rec = abs(exit_y-y)
            corner = [max(exit_x - rec, 0), min(exit_y, y)]

        elif y==exit_y:
            rec = abs(exit_x-x)
            corner = [min(exit_x, x), max(exit_y - rec, 0)]

        else:
            rec = max(abs(exit_x-x),abs(exit_y-y))
            corner = [max(max(exit_x, x) - rec, 0), max(max(exit_y, y) - rec, 0)]
        
        # CHECK POINT. 가장 작은 정사각형 구하는 과정 잘못생각했었음 
        # 단순히 출구랑 플레이어 거리 중 가장 짧은 거리 생각함 
        spot_candi.append([rec,corner[0],corner[1],x,y])

    spot_candi = sorted(spot_candi)

    return spot_candi[0]


def rotate90(x,y,rec,exit_x,exit_y):
    rc = [ [0 for _ in range(rec+1)] for _ in range(rec+1)]
    # 기존 player 위치에 업데이트하면 in players 구문에서 돌았던 애 또 돔
    rotate_players={}
    for i in range(rec+1):
        for j in range(rec+1):
            # 출구도 회전
            if [x+i,y+j] == [exit_x,exit_y]:
                # 여기서 파라미터로 받은 인자를 같은 변수명으로 바꿔버리면 바꾼 출구에 대해서 또 if 문이 걸림
                nexit_x = x+j
                nexit_y = y+rec-i
            # 플레이어도 회전
            if (x+i,y+j) in players:
                ps = players[(x+i,y+j)]
                del players[x+i,y+j]
                rotate_players[(x+j,y+rec-i)]=ps

            if maze[x+i][y+j]>0:
                rc[j][rec-i] = maze[x+i][y+j]-1
            else:
                rc[j][rec-i] = maze[x+i][y+j]

    for np in rotate_players:
        try:
            players[np].append(rotate_players[np])
        except:
            players[np] = rotate_players[np]

    for i in range(rec+1):
        for j in range(rec+1):
            maze[x+i][y+j]=rc[i][j]

    return nexit_x,nexit_y
# 초기 생성
distance_board = bfs(exit_x,exit_y)
turn = 0
answer=0
while turn < K :
    if len(players)==0:
        break
    # 0. 출구로부터 최단거리구하기
    distance_board = bfs(exit_x,exit_y)

    # 1. 플레이어 동시 이동 & 플레이어 위치 업데이트
    print("이동 전 :",players)
    players,moved = move_players()
    print("이동 후 :",players)
    print("이동 :",moved)
    answer+=moved
    if len(players)==0:
        break
    # print(f"{turn+1}에 {answer}번 움직임")
    # 2. 가장 가까이에 있는 플레이어 구하기
    mini = find_spot()
    rec_length, rx, ry, tx, ty = mini[0],mini[1],mini[2],mini[3],mini[4]
    print("출구 위치: ",exit_x,exit_y)
    print("출구와 가까운 플레이어 위치: ",tx,ty)

    # 3. 미로 회전
    print("회전 시작점과 크기 :",rx,ry,rec_length)
    exit_x,exit_y=rotate90(rx,ry,rec_length,exit_x,exit_y)
    print("회전 후 출구 위치: ",exit_x,exit_y)
    print("회전 후 플레이어 위치: ",players)
    turn+=1
    print()
print(answer)
print(exit_x+1,exit_y+1)
