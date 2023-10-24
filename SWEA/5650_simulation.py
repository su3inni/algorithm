t = int(input())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

block_type={
    1:[1,3,0,2],
    2:[3,0,1,2],
    3:[2,0,3,1],
    4:[1,2,3,0],
    5:[1,0,3,2]
}

def game(x,y,current_direction):
    global max_cnt
    cnt=0
    sr,sc = x,y
    while(1):
        nx = x + dx[current_direction]
        ny = y + dy[current_direction]
        if 0<=nx<N and 0<=ny<N:
            if board[nx][ny]==-1:
                max_cnt = max(cnt,max_cnt)
                return
            if sr==nx and sc==ny :
                max_cnt = max(cnt,max_cnt)
                return

            # 범위 내에 있고,
            # 4가지 유형 블럭
            if 1<=board[nx][ny]<=5:
                current_direction = block_type[board[nx][ny]][current_direction]
                cnt+=1
                x,y=nx,ny
            # 웜홀이라면
            elif 6<=board[nx][ny]<=10:
                for li in whole[board[nx][ny]]:
                    if (li[0],li[1]) != (nx,ny):
                        x,y = li[0],li[1]
                        break
            elif board[nx][ny]==0:
                x,y=nx,ny

        else:
            current_direction=block_type[5][current_direction]
            cnt+=1
            ####??????
            # 벽에 부딪히고 처음 위치로 돌아오면 끝나야하므로..?
            x,y=nx,ny


for tc in range(t):
    N = int(input())

    board = [ list(map(int,input().split())) for _ in range(N)]

    whole={6:[],7:[],8:[],9:[],10:[]}
    for i in range(N):
        for j in range(N):
            if 6<=board[i][j]<=10:
                whole[board[i][j]].append([i,j])

    max_cnt=0
    for i in range(N):
        for j in range(N):
            if board[i][j]==0:
                for d in range(4):
                    game(i,j,d)

    print(f"#{tc+1} {max_cnt}")
