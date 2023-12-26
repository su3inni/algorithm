from collections import deque
N,M,C = map(int,input().split())

way_board=[list(map(int,input().split())) for _ in range(N)]

car_x,car_y = map(int,input().split())
car_x-=1
car_y-=1

# 택시 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

players = {}
for m in range(M):
    info = list(map(int,input().split()))
    # player num : [ 승객 위치 [x,y] , 목적지 위치 [x,y] ]
    # 인덱스와 같도록 변경함
    players[m+1] = [[info[0]-1,info[1]-1],[info[2]-1,info[3]-1]]

def check_distance(sx,sy):
    board = [ b[:] for b in way_board]
    visited=[ [0 for _ in range(N)] for _ in range(N)]
    visited[sx][sy]=1
    # 시작점 기준
    bfs=deque()
    bfs.append((sx,sy))
    while bfs:
        pos = bfs.popleft()

        x,y = pos[0],pos[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if way_board[nx][ny] != 1 and visited[nx][ny]!=1:
                    # print(x, y, ">", nx, ny)
                    board[nx][ny] = board[x][y]+1
                    bfs.append((nx,ny))
                    visited[nx][ny]=1
        # print(bfs)


    return board

def car_move(battery,cx,cy):
    if battery==0 :
        if len(players)!=0:
            print(-1)
        else:
            print(battery)
        return

    # CHECK POINT 1. 최단거리로 가는 길 찾은게 맞나?
    distance_board = check_distance(cx,cy)
    # print(distance_board)

    candi = []
    for p in players:
        px,py = players[p][0][0],players[p][0][1]
        # 초기 차량과 승객의 위치가 같을 때 예외처리
        # 승객의 거리까지 갈 수 있는 거리만 추가
        if distance_board[px][py]!=0 or (px==cx and py==cy):
            candi.append([distance_board[px][py],px,py,p])

    # 벽때문에 승객에게 못가는 상황에 대한 처리
    if len(candi)==0:
        print(-1)
        return
    sort_candi = sorted(candi,key=lambda x:(x[0],x[1],x[2]))
    # print(sort_candi)

    target = sort_candi[0]
    target_player = target[3]
    # print("고객 == ",target_player)
    # 고객을 태우러 가는데 배터리 부족
    if battery-target[0]<=0:
        print(-1)
        return
    battery-=target[0]
    # print("고객태운 후 배터리: ",battery)
    #
    cx,cy = target[1],target[2]
    destination_board = check_distance(cx,cy)
    des_x,des_y = players[target_player][1][0],players[target_player][1][1]
    #
    use_battery = destination_board[des_x][des_y]

    # 벽때문에 목적지에 못가는 경우에 대한
    if use_battery==0:
        print("-1")
        return
    # print("고객 태우는데 필요한 배터리: ",use_battery)
    # # 목적지까지 가는데 배터리 부족
    if battery-use_battery<0:
        print( -1)
        return
    battery+=use_battery
    # print("목적지 태운 후 리필한 배터리: ",battery)
    cx,cy = des_x,des_y

    del players[target_player]

    if len(players)==0:
        print(battery)
        return
    else:
        car_move(battery,cx,cy)

car_move(C,car_x,car_y)

# 생각못한 예외
#1. 초기 차량 위치랑 승객의 위치가 같을때
#2. 벽때문에 사람은 태우고 목적지를 못갈 때
