N,M = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]

dice = [[0,1,0],[4,2,3],[0,6,0],[0,5,0]]
dr,dc = 0,0
direction=1
dx=[-1,0,1,0]
dy=[0,1,0,-1]

from collections import deque
def count_score(r,c):
    board_num = board[r][c]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    scores = deque()
    scores.append([r,c])
    visited[r][c]=1
    cnt=1
    while True :
        if len(scores)==0:
            break
        chk = scores.popleft()
        x,y = chk[0],chk[1]
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and board[nx][ny]==board_num:
                cnt+=1
                scores.append([nx,ny])
                visited[nx][ny]=1
    return cnt

def rotate_dice(direction):
    rdice = [[0 for _ in range(3)] for _ in range(4)]
    # 위로 굴림
    if direction==0:
        fn = dice[0][1]
        for i in range(1,4):
            rdice[i-1][1] = dice[i][1]
        rdice[3][1]=fn
        rdice[1][0]=dice[1][0]
        rdice[1][2]=dice[1][2]
    # 아래로 굴림
    elif direction==2:
        fn = dice[3][1]
        for i in range(3):
            rdice[i+1][1]=dice[i][1]
        rdice[0][1]=fn
        rdice[1][0]=dice[1][0]
        rdice[1][2]=dice[1][2]
    # 우로 굴림
    elif direction==1:
        for i in range(3):
            for j in range(3):
                rdice[j][3-i-1]=dice[i][j]
        rdice[3][1]=dice[3][1]

    # 좌로 굴림
    elif direction==3:
        for i in range(3):
            for j in range(3):
                rdice[3-j-1][i] = dice[i][j]
        rdice[3][1]=dice[3][1]

    return rdice
answer=0
turn=0
while turn<M:
    ndr = dr + dx[direction]
    ndc = dc + dy[direction]
    if 0>ndr or N<= ndr or 0>ndc or ndc>=N :
        direction=(direction+2)%4
        ndr = dr + dx[direction]
        ndc = dc + dy[direction]
        
    # 주사위 맵 회전
    dice = rotate_dice(direction)

    cnt = count_score(ndr,ndc)
    board_num = board[ndr][ndc]
    answer += (cnt*board_num)
    dice_num = dice[2][1]

    if dice_num > board_num :
        direction = (direction+1)%4
    elif dice_num < board_num :
        direction -=1
        if direction<0:
            direction=3
    dr,dc = ndr,ndc
    turn+=1

print(answer)
