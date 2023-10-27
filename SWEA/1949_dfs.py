T = int(input())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,current_height,flag,count):
    global max_cnt,visited

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
            # 등산로 만들 수 있음
            if board[nx][ny]< current_height:
                visited[nx][ny]=1
                dfs(nx,ny,board[nx][ny],flag,count+1)
                visited[nx][ny]=0
            else:
                # 공사해서 등산로 만들기
                if flag==False:
                    for k in range(1,K+1):
                        if board[nx][ny]-k < current_height :
                            visited[nx][ny]=1
                            dfs(nx,ny,board[nx][ny]-k,True,count+1)
                            visited[nx][ny]=0
                # 몬만듬
                else:
                    max_cnt = max(count,max_cnt)
        else:
            max_cnt=max(count,max_cnt)


for tc in range(T):
    N,K = map(int,input().split())

    board = [ list(map(int,input().split())) for _ in range(N)]


    height_dict={}
    max_height=0
    for i in range(N):
        for j in range(N):
            if board[i][j] > max_height:
                max_height=board[i][j]
            if board[i][j] not in height_dict:
                height_dict[board[i][j]]=[[i,j]]
            else:
                height_dict[board[i][j]].append([i,j])

    # height_dict=dict(sorted(list(height_dict.items()),reverse=True))

    max_cnt=0
    for points in height_dict[max_height]:
        visited = [[0 for _ in range(N)] for _ in range(N)]
        # x,y,height,flag,cnt
        visited[points[0]][points[1]]=1
        dfs(points[0],points[1],max_height,False,1)

    print(f"#{tc+1} {max_cnt}")
