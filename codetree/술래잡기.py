N,M,H,K = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

players={}
for i in range(M):
    x,y,d = map(int,input().split())
    if d==1:
        try:
            players[(x-1,y-1)].append(1)
        except:
            players[(x-1,y-1)]=[1]
    else:
        try :
            players[(x-1,y-1)].append(2)
        except:
            players[(x-1,y-1)]=[2]

trees=[]
for i in range(H):
    x,y = map(int,input().split())
    trees.append([x-1,y-1])

def insideout_direction(x,y):
    cnt=1
    direction=0
    for j in range(N):
        for i in range(2):
            for c in range(cnt):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if nx ==0 and ny ==0:
                    catch_board[nx][ny] = (direction+1)%4
                    return
                if 0<=nx<N and 0<=nx<N:
                    catch_board[x][y]=direction
                    x ,y = nx,ny
            direction = (direction+1)%4
        cnt+=1
    # catch_board[0][0]=2

def outsidein_direction(x,y):
    cnt = N-1
    direction = 2
    for j in range(N):
        if cnt==N-1:
            repeat=3
        else:
            repeat=2
        for i in range(repeat):
            for c in range(cnt):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if nx == N//2 and ny == N//2:
                    catch_board[x][y] = direction
                    direction-=1
                    if direction<0:
                        direction=3
                    catch_board[nx][ny] = direction
                    return
                if 0 <= nx < N and 0 <= nx < N:
                    catch_board[x][y] = direction
                    x, y = nx, ny
            direction-=1
            if direction<0:
                direction=3
        cnt -= 1

    # catch_board[N//2][N//2]=0

def move_run():
    update_players={}
    for pp in players:
        for p in players[pp]:
            x,y = pp[0],pp[1]
            direction = p
            # 이동 조건
            if abs(x-cx)+ abs(y-cy) <=3:
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0<=nx<N and 0<=ny<N :
                    # CHECK POINT. 두 if 문에서 걸러지는 경우는 다르다. 
                    # if nx!=cx and ny!=cy:
                    if [nx,ny]!= [cx,cy]:
                        try:
                            update_players[(nx,ny)].append(direction)
                        except:
                            update_players[(nx,ny)] = [direction]
                    else:
                        try :
                            update_players[(x,y)].append(direction)
                        except:
                            update_players[(x,y)] = [direction]
                else:
                    direction = (direction+2)%4
                    nx = x + dx[direction]
                    ny = y + dy[direction]
                    if 0<=nx<N and 0<=ny<N:
                        if  [nx,ny]!= [cx,cy]:
                            try:
                                update_players[(nx,ny)].append(direction)
                            except:
                                update_players[(nx,ny)] = [direction]

                        else:
                            try:
                                update_players[(x,y)].append(direction)
                            except:
                                update_players[(x,y)] = [direction]
            else:
                try :
                    update_players[(x,y)].append(direction)
                except:
                    update_players[(x, y)] = [direction]

    return update_players

def catch(cx,cy,direction):
    gotcha=0
    # CHECK POINT 2. 술래가 있는 위치부터 잡기시작한다는 것! range(1,4)로 지정해서 술래가 앞 3칸을 보는 것으로 했던게 오답의 원인
    for d in range(3):
        ncx = cx + dx[direction]*d
        ncy = cy + dy[direction]*d
        if 0<=ncx<N and 0<=ncy<N :
            if (ncx,ncy) in players :
                if [ncx,ncy] not in trees:
                    gotcha+=len(players[(ncx,ncy)])
                    del players[(ncx,ncy)]

    return gotcha


turn = 1
answer=0
cx,cy = N//2,N//2

while turn<=K :
    if cx == 0 and cy == 0:
        catch_board = [[0 for _ in range(N)] for _ in range(N)]
        outsidein_direction(cx,cy)
    elif cx==N//2 and cy==N//2:
        catch_board = [[0 for _ in range(N)] for _ in range(N)]
        insideout_direction(cx,cy)

    # m명의 도망자 움직이기
    update_players = move_run()
    players = update_players

    # 술래 이동
    cd = catch_board[cx][cy]
    ncx = cx + dx[cd]
    ncy = cy + dy[cd]

    catch_direction = catch_board[ncx][ncy]

    # 잡기
    gotcha = catch(ncx,ncy,catch_direction)
    answer += (turn*gotcha)
    cx ,cy = ncx,ncy


    turn+=1

print(answer)

# 한 칸에 여러명 있는 경우 생각하기 
# 술래가 움직여야할 자리에 도망자가 있으면..? >> 3칸 위치 어디서부터 시작인지 잘보기!!! 
