T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
for t in range(T):
    arr=[]
    N = int(input())
    for _ in range(N):
        r=[]
        s = input()
        for ss in s:
            r.append(int(ss))
        arr.append(r)

    dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    dist[0][0]=0

    # priority queue로 구현하는 경우
    from queue import PriorityQueue
    check = PriorityQueue()
    check.put((0,0,0))

    while check.qsize():
        distance,x,y = check.get()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<N and 0<=ny<N:
                if dist[nx][ny] > distance + arr[nx][ny]:
                    dist[nx][ny] = distance + arr[nx][ny]
                    check.put((dist[nx][ny],nx,ny))


    # heapq 로 구현하는 경우
    # import heapq
    # check=[]
    # heapq.heappush(check,(0,0,0))
    #
    # while check:
    #     distance,x,y = heapq.heappop(check)
    #     for d in range(4):
    #         nx = x + dx[d]
    #         ny = y + dy[d]
    #         if 0<=nx<N and 0<=ny<N:
    #             if dist[nx][ny] > distance + arr[nx][ny]:
    #                 dist[nx][ny] = distance+arr[nx][ny]
    #                 heapq.heappush(check,(dist[nx][ny],nx,ny))

    ## bfs로 구현하는 경우
    # from collections import deque
    # check=deque()
    # check.append([0,0])
    #
    # while 1:
    #     if len(check)==0:
    #         break
    #     current = check.popleft()
    #     x,y = current[0],current[1]
    #     for d in range(4):
    #         nx = x + dx[d]
    #         ny = y + dy[d]
    #         if 0<=nx<N and 0<=ny<N :
    #             if dist[nx][ny] > dist[x][y]+arr[nx][ny] :
    #                 dist[nx][ny] = dist[x][y]+arr[nx][ny]
    #                 check.append([nx,ny])

    # for dd in dist:
    #     print(dd)
    print(f"#{t+1} {dist[N-1][N-1]}")
