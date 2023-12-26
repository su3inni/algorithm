# 너무 어렵게 시작하려고 했음
# deque를 쓰려고 했던 이유는 도둑말이 번호 순서대로 움직여야하고 술래에 잡히면 넣고 빼야 했기 때문에
# 삽입 삭제가 용이한 자료구조를 사용하려고 했었음
# 근데..이게 더 음.. swap하는 과정에서 빼고 다시 넣을 때 그 위치로 넣어지는게 아니라 맨 뒤로 추가돼서.. 하튼 필요없었음
# from collections import deque

board = [ [0,0,0,0] for _ in range(4)]
# 방향을 잘..설정하고 반시계방향이나 시계방향으로 움직일 때 원점으로 다시 돌아오는 걸 헷갈리지 않으려면 다른 원소 끼면 안됨
# 예를 들어 아래처럼 설정하면 안됨
# 0, ↑, ↖, ←, ↙, ↓, ↘, →, ↗
# dx = [0,-1,-1,0,1,1,1,0,-1]
# dy = [0,0,-1,-1,-1,0,1,1,1]

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

for x in range(4):
    row = list(map(int,input().split()))
    for y in range(0,7,2):
        # 번호, 방향
        board[x][y//2]=[row[y],row[y+1]-1]

# 도둑들 이동
def mvthfs(board,thfs):
    for n in thfs:
        x,y=0,0
        direction=0
        for i in range(4):
            for j in range(4):
                if board[i][j][0]==n:
                    direction = board[i][j][1]
                    x=i
                    y=j
                    break

        # print(n,">",x,",",y)
        for d in range(8):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if ( nx<0 or nx>3) or (ny<0 or ny>3) or board[nx][ny][0]==100:
                # print("direction :",direction)
                direction = (direction+1)%8
                # print("direction change",direction)
            elif 1<=board[nx][ny][0]<=16:
                # swap
                board[x][y] = board[nx][ny]
                board[nx][ny]= [n,direction]
                break
            else:
                # POINT 1: swap 할 때 빼놓은 곳 없는지 확인
                board[x][y]=[0,0]
                board[nx][ny]=[n,direction]
                break

        # for i in range(4):
        #     print(board[i])


def mvtagger(board,thfs,tagger,score):
    global max_score
    # 도둑들 움직임
    mvthfs(board,thfs)

    cx,cy = tagger[0],tagger[1]
    cdirection = tagger[2]

    target_candi=[]
    while True:
        ncx = cx+dx[cdirection]
        ncy = cy+dy[cdirection]
        if (0>ncx or 3<ncx) or ( 0>ncy or 3<ncy):
            break
        elif 1<=board[ncx][ncy][0]<=16:
            target_candi.append(board[ncx][ncy][0])
        cx = ncx
        cy = ncy
    # print("TAGGER : ",tagger[0],tagger[1],cdirection)
    # print("target list",target_candi)

    if len(target_candi)==0:
        if score > max_score:
            max_score=score
        # print(max_score)
        # print("===================================")
        return

    for target in target_candi:
        # print("TARGET:",target)
        # POINT2 : 재귀로 게임이 진행될 때 복사해서 진행하기
        # POINT3 : 복사해야할 원소가 맵과 업데이트되는 도둑들 말이라는 것까지
        copy_board = [ b[:] for b in board ]
        copy_thfs = thfs[:]

        for i in range(4):
            for j in range(4):
                if copy_board[i][j][0]==target:
                    # POINT4 : 술래말이 있던 곳의 좌표 확인하기
                    # 처음에 cx,cy를 넣었는데 위의 알고리즘에서 업데이트가 되었기 때문에 엉뚱한 곳에 술래말을 두었음
                    copy_board[tagger[0]][tagger[1]]=[0,0]
                    copy_board[i][j]=[100,copy_board[i][j][1]]
                    copy_thfs.remove(target)
                    # 재귀하는 곳에 파라미터로 직접 넣어서 복구 시키는 일 없도록 함
                    mvtagger(copy_board,copy_thfs,[i,j,copy_board[i][j][1]],score+target)
                    break

# 시작점 고정
max_score=0
max_score+=board[0][0][0]

# 술래 설정
# x, y, 방향
tagger = [0,0,board[0][0][1]]
thfs=[i for i in range(1,17)]
thfs.remove(board[0][0][0])
board[0][0]=[100,board[0][0][1]]

mvtagger(board,thfs,tagger,max_score)

print(max_score)