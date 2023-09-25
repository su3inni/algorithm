T = int(input())

def count_dessert(pre_direction,cnt,x,y,path):
    global i,j,ans
    if cnt>4 :
        return
    if cnt==4 and x==i and y==j:
        ans=max(ans,len(path))
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        # if 0<=nx<N and 0<=ny<N and cnt==4 and nx==i and ny==j:
        #     print("되돌아옴", i,j,">",path)
        #     ans = max(ans, len(path))
        #     return
        if (0<=nx<N and 0<=ny<N)  :
            if cafe_map[nx][ny] not in path:
                if d==pre_direction :
                    # print("유지",path)
                    visited[nx][ny]=1
                    path.append(cafe_map[nx][ny])
                    count_dessert(d,cnt,nx,ny,path)
                    visited[nx][ny]=0
                    path.pop()
                elif pre_direction != ((4-d)-1) :
                    cnt+=1
                    visited[nx][ny]=1
                    path.append(cafe_map[nx][ny])
                    # print("방향전환",nx,ny,path)
                    count_dessert(d,cnt,nx,ny,path)
                    visited[nx][ny]=0
                    path.pop()
                    cnt-=1
    return

for tc in range(T):
    N = int(input())

    cafe_map = [ list(map(int,input().split()) )for _ in range(N)]

    # 0: 좌상 , 1: 우상 , 2:좌하 , 3:우하
    dx = [-1,-1,1,1]
    dy = [-1,1,-1,1]

    ans = -1
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # print("시작지점",i,j)
            visited[i][j]=1
            count_dessert(-1,0,i,j,[])
            visited[i][j]=0
            # print("------")
    print(f"#{tc+1} {ans}")
