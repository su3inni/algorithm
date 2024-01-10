N,M,K = map(int,input().split())
gun_board=[]
for _ in range(N):
    guns = list(map(int,input().split()))
    cnts=[]
    for g in guns :
        if g==0:
            cnts.append([])
        else:
            cnts.append([g])
    gun_board.append(cnts)


players=[]
for i in range(M):
    p = list(map(int,input().split()))
    x,y,d,s = p[0]-1, p[1]-1,p[2],p[3]
    players.append([i,x,y,d,s,0])

# ↑, →, ↓, ←
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def get_guns(num,x,y):
    print("총획득")
    gun_power = gun_board[x][y][0]
    # 플레이어가 총을 가지고 있지 않음
    if players[num][5] == 0 :
        gun_board[x][y].remove(gun_power)
        players[num][5]=gun_power
    # 플레이어가 총을 가지고 있음
    else:
        player_gun = players[num][5]
        if player_gun < gun_power:
            gun_board[x][y].remove(gun_power)
            gun_board[x][y].append(player_gun)
            gun_board[x][y].sort(reverse=True)
            players[num][5] = gun_power

def loser_move(num,x,y):
    loser = players[num]
    # lx,ly = loser[1],loser[2]
    ld = loser[3]
    gun = loser[5]
    # 총 내려놓기
    if gun!=0:
        gun_board[x][y].append(gun)
        gun_board[x][y].sort(reverse=True)
        loser[5]=0

    # 이동하기
    for d in range(4):
        nx = x + dx[ld]
        ny = y + dy[ld]
        if (nx,ny) in position or 0>nx or N<=nx or 0>ny or N<=ny :
            ld = (ld+1)%4
        else:
            print(position)
            print("진사람 이동",num,":",x,y,">",nx,ny)
            # 이동한 곳에 총이 있으면
            if len(gun_board[nx][ny])!=0:
                get_guns(num,nx,ny)

            position[(nx,ny)] = num
            players[num][1]=nx
            players[num][2]=ny
            players[num][3]=ld
            break

def fight(num,x,y):
    print("싸움")
    current_player = players[num]
    target_num = position[(x,y)]
    target_player = players[target_num]

    self_power,gun_power = current_player[4],current_player[5]
    tself_power,tgun_power = target_player[4],target_player[5]

    if self_power + gun_power > tself_power + tgun_power:
        score = (self_power + gun_power) - (tself_power + tgun_power)
        answer[num]+=score

        # 진사람 움직이고
        loser_move(target_num,x,y)
        if len(gun_board[x][y])!=0:
            get_guns(num,x,y)

        players[num][1]=x
        players[num][2]=y
        position[(x,y)]=num

    elif self_power + gun_power < tself_power + tgun_power:
        score = (tself_power + tgun_power) -  (self_power + gun_power)
        answer[target_num]+=score

        loser_move(num,x,y)
        if len(gun_board[x][y])!=0:
            get_guns(target_num,x,y)

    # 합이 똑같으면
    else:
        if self_power > tself_power:
            loser_move(target_num, x, y)
            if len(gun_board[x][y]) != 0:
                get_guns(num, x, y)

            position[(x, y)] = num
            players[num][1]=x
            players[num][2]=y
        else:
            loser_move(num, x, y)
            if len(gun_board[x][y]) != 0:
                get_guns(target_num, x, y)

answer=[0 for _ in range(M)]
turn=0
while turn < K :
    players = sorted(players,key= lambda x: x[0] )
    position = { (p[1],p[2]):p[0] for p in players }
    print(players)
    print(position)

    for p in players :
        num=p[0]
        x,y = p[1],p[2]
        print("MOVE",num,"in",x,y)
        del position[((x,y))]

        direction = p[3]
        power = p[4]
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0>nx or nx>=N or 0>ny or ny>=N:
            direction = (direction+2)%4
            nx = x + dx[direction]
            ny = y + dy[direction]
            p[3]=direction

        # 이동한 공간에 플레이어가 없다면
        if (nx,ny) not in position:
            guns = gun_board[nx][ny]
            # 총이 있다면
            if len(guns)!=0:
                get_guns(num,nx,ny)
            p[1] = nx
            p[2] = ny
            position[(nx,ny)]=num

        # 이동한 공간에 플레이어가 있다면
        # 싸워야함
        else:
            fight(num,nx,ny)

        for g in gun_board:
            print(g)
        print(players)
        print(position)
        print()
    turn+=1

print()
print(answer)
