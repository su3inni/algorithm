# 복잡한 테스트 케이스가 틀렸을 때
# 내가 작성한 알고리즘을 다시 정리해서 손으로 작성해보고
# 문제를 다시 읽으며 놓친 조건이 있는지, 잘못 구성한 로직이 있는지 검토한다

N,M,K,C = map(int,input().split())

tree_board = []
status_board = [[0 for _ in range(N)] for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
rdx = [-1,-1,1,1]
rdy = [-1,1,1,-1]

for i in range(N):
    tree_board.append(list(map(int,input().split())))


def tree_growth():
    # 인접한 나무 수만큼 성장
    for i in range(N):
        for j in range(N):
            neighbor=0
            for d in range(4):
                nx = i+dx[d]
                ny = j+dy[d]
                if 0<=nx<N and 0<=ny<N:
                    # 인접한 나무 확인
                    if tree_board[nx][ny]>0 and status_board[nx][ny]==0:
                        neighbor+=1
            if tree_board[i][j]>0:
                tree_board[i][j]+=neighbor

def tree_spread():
    # 벽이 아니고 제초제가 안뿌려져있고 다른 나무 없는 경우 번식
    cum_board=[[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if tree_board[i][j] > 0 :
                can_spread=0
                for d in range(4):
                    nx = i+dx[d]
                    ny = j+dy[d]
                    if 0<=nx<N and 0<=ny<N:
                        # 나무 있는 공간에서
                        # 빈 공간이고 제초제 안뿌려져있으면
                        if tree_board[nx][ny]==0 and status_board[nx][ny]==0:
                            can_spread+=1
                if can_spread!=0:
                    spread_count = tree_board[i][j]//can_spread
                    for d in range(4):
                        nx = i+dx[d]
                        ny = j+dy[d]
                        if 0<=nx<N and 0<=ny<N:
                            # 빈 공간이고 제초제 안뿌려져있으면
                            if tree_board[nx][ny]==0 and status_board[nx][ny]==0:
                                cum_board[nx][ny]+=spread_count

    for i in range(N):
        for j in range(N):
            tree_board[i][j]+=cum_board[i][j]

def find_max_remove():
    max_remove=0
    x ,y = 0,0
    for i in range(N):
        for j in range(N):
            remove=0
            if tree_board[i][j]>0:
                remove+=tree_board[i][j]
                for d in range(4):
                    for k in range(1, K + 1):
                        nx = i+rdx[d]*k
                        ny = j+rdy[d]*k
                        if 0<=nx<N and 0<=ny<N :
                            if tree_board[nx][ny]>0:
                                remove+=tree_board[nx][ny]
                            # 나무가 없거나 벽인 경우
                            elif tree_board[nx][ny]<=0:
                                break
            if remove > max_remove:
                x = i
                y = j
                max_remove = remove
    return x,y

def count_remove(x,y):
    if tree_board[x][y]<0:
        return 0

    removed=tree_board[x][y]
    tree_board[x][y]=0
    status_board[x][y]=C+1

    for d in range(4):
        for k in range(1,K+1):
            nx  = x+rdx[d]*k
            ny = y + rdy[d]*k
            if 0<=nx<N and 0<=ny<N:
                if tree_board[nx][ny]>0:
                    # 제거하고 제초제 뿌려
                    removed += tree_board[nx][ny]
                    tree_board[nx][ny]=0
                    status_board[nx][ny] = C + 1
                elif tree_board[nx][ny] < 0:
                    break
                elif tree_board[nx][ny]==0:
                    status_board[nx][ny] = C + 1
                    break

    return removed

def time_pass():
    for i in range(N):
        for j in range(N):
            if status_board[i][j]>0:
                status_board[i][j]-=1

answer=0
year=1
while year<=M:
    time_pass()

    tree_growth()
    print("나무 성장")
    for i in range(N):
        print(tree_board[i])

    tree_spread()
    print("나무번식")
    for i in range(N):
        print(tree_board[i])

    max_x,max_y = find_max_remove()
    print("가장 많이 제거되는 위치 > ",max_x,max_y)

    removed_tree = count_remove(max_x,max_y)
    answer+=removed_tree
    print("제거된 나무 수 >",removed_tree)
    # for i in range(N):
    #     print(status_board[i])

    year+=1

print(answer)
