L,N,Q = map(int,input().split())

chs_board = [ list(map(int,input().split())) for _ in range(L)]

players={}
for i in range(N):
    x,y,h,w,k = map(int,input().split())
    players[i+1] = [x-1,y-1,h,w,k,0]

def pls_area():
    pls_board = [[0 for _ in range(L)] for _ in range(L)]
    areas={}
    for p in players:
        r,c = players[p][0],players[p][1]
        w,h = players[p][2],players[p][3]
        for i in range(w):
            for j in range(h):
                try:
                    areas[p].append([r+i,c+j])
                except:
                    areas[p]=[[r+i,c+j]]
                pls_board[r+i][c+j]=p
    return areas,pls_board

dx = [-1,0,1,0]
dy = [0,1,0,-1]
# CHECK POINT. move_pls 이동 가능한 플레이어를 재귀로 돌 때마다 추가해줘야되므로 인자로 넘기기 
def possible_move(i,d,area,move_pls):
    for ox,oy in area:
        x,y = ox,oy
        visited[x][y]=1
        # 이동 가능한지 연쇄적으로 확인하기
        while True:
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<L and 0<=ny<L:
                # 벽이 있으면 못움직임
                if chs_board[nx][ny]==2:
                    return False,[]
                # 벽이 아니고
                else:
                    # 기사가 있으면
                    if pls_board[nx][ny]!=0:
                        if pls_board[nx][ny]!=i and visited[nx][ny]==0:
                            visited[nx][ny] = 1
                            checkflag,movepls = possible_move(pls_board[nx][ny],d,areas[pls_board[nx][ny]],move_pls)
                            if checkflag:
                                move_pls.append(pls_board[nx][ny])
                            else:
                                return False,[]
                        x,y = nx,ny
                    # 기사가 없으면 이동 가능
                    if pls_board[nx][ny]==0:
                        break
            else:
                return False,[]


    return True, set(move_pls)

def move_players(movepls,d):
    for p in movepls:
        r,c,h,w,k,dm = players[p]
        nr = r + dx[d]
        nc = c + dy[d]
        players[p] = [nr,nc,h,w,k,dm]

def check_health(mp,ar):
    minus=0
    for ax,ay in ar:
        if chs_board[ax][ay]==1:
            minus+=1

    players[mp][4]-=minus
    players[mp][5]+=minus

    if players[mp][4]<=0:
        del players[mp]

turn=0
answer=0
while turn<Q:
    i,d = map(int,input().split())
    # 현재 기사들의 면적 구하기
    areas,pls_board = pls_area()

    # CHECK POINT
    if i in players:
        visited = [[0 for _ in range(L)] for _ in range(L)]
        checkflag,movepls = possible_move(i,d,areas[i],[])
        movepls = list(movepls)
        if checkflag:
            if len(movepls)>0 :
                # 영향받은 기사들 이동
                move_players(movepls+[i],d)
                # 이동 후 면적 다시 구하고
                areas,pls_board = pls_area()
                # 함정에 따른 체력
                for mp in movepls:
                    check_health(mp,areas[mp])
            else:
                move_players([i],d)

    turn+=1

for p in players:
    answer+=players[p][5]
print(answer)
