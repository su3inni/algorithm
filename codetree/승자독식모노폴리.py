dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]
N,M,K = map(int,input().split())

board = [ list(map(int,input().split())) for _ in range(N)]

direction = list(map(int,input().split()))

player_direction_priority=[]
for m in range(M):
    priority=[]
    # 위,아래,왼쪽,오른쪽
    for d in range(4):
        priority.append(list(map(int,input().split())))
    player_direction_priority.append(priority)


# 초기 설정하면서
# 초기 player 위치 설정
player_dict={}
for n in range(1,M+1):
    x,y=0,0
    for i in range(N):
        for j in range(N):
            if board[i][j]==n:
                board[i][j]=[n,K]
                x=i
                y=j
                break
    player_dict[n]=[[x,y],direction[n-1]]

for i in range(N):
    for j in range(N):
        if board[i][j]==0:
            board[i][j]=[0,0]

def play():
    score=-1

    while True:
        if score>1000:
            print(-1)
            return
        if len(player_dict)==1:
            print(score+1)
            return

        wait_list={}
        for player in player_dict:
            player_curr = player_dict[player][1]
            x,y = player_dict[player][0]
            get_flag=False
            for d in range(4):
                nx = x + dx[player_direction_priority[player-1][player_curr-1][d]]
                ny = y + dy[player_direction_priority[player-1][player_curr-1][d]]
                if 0<=nx<N and 0<=ny<N :
                    if board[nx][ny][0]==0:
                        try:
                            wait_list[(nx,ny)].append([player,player_direction_priority[player-1][player_curr-1][d]])

                        except:
                            wait_list[(nx,ny)]=[[player,player_direction_priority[player-1][player_curr-1][d]]]
                        get_flag=True
                        break

                else:
                    continue

            # 새로 계약할 공간이 없으면
            if get_flag==False:
                for dd in range(4):
                    nx = x + dx[player_direction_priority[player - 1][player_curr - 1][dd]]
                    ny = y + dy[player_direction_priority[player - 1][player_curr - 1][dd]]
                    if 0<=nx<N and 0<=ny<N and board[nx][ny][0]==player:
                            board[nx][ny]=[player,K]
                            player_dict[player]=[[nx,ny],player_direction_priority[player - 1][player_curr - 1][dd]]
                            break


        for w in wait_list:
            if len(wait_list[w])==1:
                x,y = w[0],w[1]
                board[x][y]=[wait_list[w][0][0],K]
                player_dict[wait_list[w][0][0]]=[[x,y],wait_list[w][0][1]]
            else:
                sorted_wait =sorted(wait_list[w],key=lambda x:x[0])
                x,y = w[0],w[1]
                board[x][y]=[sorted_wait[0][0],K]
                player_dict[sorted_wait[0][0]][0]=[x,y]
                # POINT 2. 방향도 새로고침 해야함
                player_dict[sorted_wait[0][0]][1]=sorted_wait[0][1]
                for rm in sorted_wait[1:]:
                    # POINT 3. 문제 잘 읽어야함
                    # rmx,rmy = player_dict[rm[0]][0]
                    # board[rmx][rmy]=[0,0]
                    player_dict.pop(rm[0])

        # POINT 1. 실행 순서 잘 고려하기
        # POINT 4. 실행해야될 칸이 어딘지 다시 확인하기
        curr = [ player_dict[p][0] for p in player_dict]
        for i in range(N):
            for j in range(N):
                if board[i][j][1]>0:
                    if [i, j] not in curr:
                        board[i][j][1]-=1
                    # 유효기간 끝?
                    if board[i][j][1]==0:
                        board[i][j]=[0,0]

        score+=1

play()