N,M,K = map(int,input().split())

board=[]
for i in range(N):
    info = list(map(int,input().split()))
    board.append(info)

total_top=[]
exist_top=[]
for i in range(N):
    for j in range(M):
        if board[i][j]!=0:
            exist_top.append([i,j])
            # [ 공격력 , turn, x+y, x,y ]
            total_top.append([board[i][j],0,i+j,i,j])

def find_attacker(total_top):
    sort_top = sorted(total_top,key = lambda x: (x[0],-x[1],-x[2],-x[4]))
    sort_top[0][0] += ( N+M )
    return sort_top

def find_target(rest_tops):
    sort_rest = sorted(rest_tops,key=lambda x:(-x[0],x[1],x[2],x[4]))
    return sort_rest[0][3],sort_rest[0][4]

from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(x,y):
    distance_board=[[0 for _ in range(M)]for _ in range(N)]
    visited=[[0 for _ in range(M)] for _ in range(N)]
    tops= deque()
    tops.append([x,y])
    visited[x][y]=1

    while True:
        if len(tops)==0:
            break
        target = tops.popleft()
        tx,ty = target[0],target[1]
        for d in range(4):
            nx = tx + dx[d]
            ny = ty + dy[d]
            if 0<=nx<N and 0<=ny<M :
                if visited[nx][ny]==0 and [nx,ny] in exist_top:
                    distance_board[nx][ny] = distance_board[tx][ty]+1
                    tops.append([nx,ny])
                    visited[nx][ny]=1
            else:
                if nx >= N :
                    nx = nx%N
                elif nx < 0 :
                    nx = N-1
                if ny >= M :
                    ny = ny%M
                elif ny < 0 :
                    ny = M-1
                if visited[nx][ny]==0 and [nx,ny] in exist_top :
                    distance_board[nx][ny] = distance_board[tx][ty]+1
                    tops.append([nx,ny])
                    visited[nx][ny]=1
    return distance_board

def lazer_attack(ax,ay,tx,ty):
    hist = []
    visited = [ [0 for _ in range(M)] for _ in range(N)]
    path = deque()
    path.append([ax,ay])
    visited[ax][ay]=1

    while True:
        min_di = 1000
        # if len(path)==0:
        #     return False, []
        points = path.popleft()
        ax,ay = points[0],points[1]

        for d in range(4):
            nx = ax + dx[d]
            ny = ay + dy[d]
            if nx >= N:
                nx = nx % N
            elif nx < 0:
                nx = N - 1
            if ny >= M:
                ny = ny % M
            elif ny < 0:
                ny = M - 1

            if nx == tx and ny == ty :
                return True, hist

            # if min_di > distance_board[nx][ny] and distance_board[nx][ny]!=0:
            if min_di > distance_board[nx][ny] and [nx,ny] in exist_top and distance_board[nx][ny]!=0:
                min_di = distance_board[nx][ny]
                minx ,miny = nx,ny

        if min_di==1000:
            return False,[]

        ax,ay = minx,miny

        if visited[ax][ay]==0:
            hist.append([ax, ay])
            path.append([ax,ay])
            visited[ax][ay]=1


    return False,[]

def change_power(power,tx,ty,pass_tops):
    update_tops = []
    for t in total_top:
        if [t[3],t[4]] == [tx,ty] :
            t[0]-=power
            if t[0] <= 0 :
                exist_top.remove([tx,ty])
            else:
                update_tops.append(t)
        elif [t[3],t[4]] in pass_tops:
            t[0]-= power//2
            if t[0]<=0:
                exist_top.remove([t[3],t[4]])
            else:
                update_tops.append(t)
        else:
            update_tops.append(t)
    return update_tops

bdx = [-1,-1,-1,0,0,1,1,1]
bdy = [-1,0,1,-1,1,-1,0,1]

def bomb_attack(ax,ay,tx,ty):
    pass_tops = []
    for d in range(8):
        nx = tx + bdx[d]
        ny = ty + bdy[d]
        if nx >= N:
            nx = nx % N
        elif nx < 0:
            nx = N - 1
        if ny >= M:
            ny = ny % M
        elif ny < 0:
            ny = M - 1
        # CHECK POINT : 포탄 터지는 반경에 공격자가 있는 경우 고려하기
        if [nx,ny] in exist_top and [nx,ny]!=[ax,ay]:
            pass_tops.append([nx,ny])
    return pass_tops

def strength_tops(ax,ay,tx,ty,pass_tops):
    eff = pass_tops + [[ax,ay]] + [[tx,ty]]
    for t in total_top :
        if [t[3],t[4]] not in eff :
            t[0]+=1

turn=0
while turn<K :
    if len(total_top)==1:
        break

    # 공격자 선정 및 공격력 강화
    total_top = find_attacker(total_top)
    attacker = total_top[0]
    # 최근 공격자 표시
    total_top[0][1]=turn+1
    ax, ay = attacker[3],attacker[4]
    power = attacker[0]

    # 타겟 선정
    tx,ty = find_target(total_top[1:])
    # 타겟으로부터 최단거리
    distance_board = bfs(tx,ty)

    attack = False
    attack , pass_tops= lazer_attack(ax,ay,tx,ty)

    if attack==False:
        pass_tops = bomb_attack(ax,ay,tx,ty)

    total_top = change_power(power, tx, ty, pass_tops)

    # 정비
    strength_tops(ax,ay,tx,ty,pass_tops)
    turn+=1


answer_tops = sorted(total_top,key = lambda x: (-x[0],x[1],x[2],x[4]))
answer = answer_tops[0]
print(answer[0])
