from collections import deque
N, M = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]
target =[list(map(int,input().split())) for _ in range(M)]

basecamp=[]
for i in range(N):
    for j in range(N):
        if board[i][j]==1:
            basecamp.append([i,j])

player_target={}
for i in range(M):
    player_target[i] = [target[i][0]-1,target[i][1]-1]

dx = [-1,0,0,1]
dy = [0,-1,1,0]
time=0
complete=0
in_player={}
ban_position=[]

def bfs(x,y):
    distance_record=[[0 for _ in range(N)] for _ in range(N)]
    visited=[[0 for _ in range(N)] for _ in range(N)]
    visited[x][y]=1
    points = deque()
    points.append([x,y])

    while True:
        if len(points)==0:
            break
        p = points.popleft()
        x,y = p[0],p[1]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and [nx,ny] not in ban_position:
                distance_record[nx][ny] = distance_record[x][y]+1
                points.append([nx,ny])
                visited[nx][ny]=1

    return distance_record

# 초기 최단거리 
distance_record = []
for p in player_target:
    distance_board = []
    tx, ty = player_target[p][0], player_target[p][1]
    distance_history = bfs(tx, ty)
    distance_record.append(distance_history)

def move_inplayer():
    min_direction = 0
    for p in in_player:
        x,y = in_player[p][0],in_player[p][1]
        check_distance = distance_record[p]
        move_list=[]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<N and [nx,ny] not in ban_position:
                move_list.append([check_distance[nx][ny],nx,ny])

        move_list = sorted(move_list,key = lambda x:x[0])
        mx,my = move_list[0][1] ,move_list[0][2]
        in_player[p] = [mx,my]

def add_player(time):
    check_distance = distance_record[time]
    min_di =100
    min_x,min_y = 0,0
    for base in basecamp:
        bx,by = base[0],base[1]
        # CHECK POINT2 :  최단 거리로 베이스 캠프 정할 때 갈수 없는 곳은 0인데 이 부분을 베이스 캠프로 지정하지 않도록 한다. 
        if min_di > check_distance[bx][by] and check_distance[bx][by]!=0:
            min_x,min_y = bx,by
            min_di = check_distance[bx][by]
    return min_x,min_y

def check_arrive(complete):
    update_player={}
    for p in in_player:
        px,py = in_player[p][0],in_player[p][1]
        if px == player_target[p][0] and py == player_target[p][1]:
            ban_position.append([px,py])
            complete+=1
        else:
            update_player[p]=[px,py]
    return update_player,complete


while True:
    # 모두 편의점에 도착
    if complete==M:
        break

    #1. 격자 내 사람들 이동
    if len(in_player)!=0:
        move_inplayer()

    # 2. 편의점 도착한 경우 멈추기
    in_player,complete = check_arrive(complete)
    
    # CHECK POINT3 : ban_position 업데이트 후에 다시 최단경로 구해야한다. 
    new_distance_record = []
    for p in player_target:
        distance_board = []
        tx, ty = player_target[p][0], player_target[p][1]
        distance_history = bfs(tx, ty)
        new_distance_record.append(distance_history)
    distance_record = new_distance_record

    # 3. 플레이어 추가할 때 가까운 베이스캠프로 넣기
    if time<M:
        # CHECK POINT1 : 초기에 한 번 최단거리를 구하는 것이 아니라 매번 구해야한다. ban_position 업데이트에 따라
        new_distance_record = []
        for p in player_target:
            distance_board = []
            tx, ty = player_target[p][0], player_target[p][1]
            distance_history = bfs(tx, ty)
            new_distance_record.append(distance_history)

        distance_record = new_distance_record

        min_x,min_y = add_player(time)
        in_player[time] = [min_x,min_y]
        basecamp.remove([min_x,min_y])
        ban_position.append([min_x,min_y])
    time+=1

print(time)
