from collections import deque
T = int(input())

for tc in range(T) :
    # 지도크기 세로,가로 / 맨홀위치 세로,가로 / 탈출 시간
    N,M,R,C,L = map(int,input().split())

    # 파이프구조 상하좌우
    # 0번은 파이프없는 것을 뜻하니 [0,0,0,0]을 추가하는 것이 좋음
    pipe_types=[[0,0,0,0],[1,1,1,1],[1,1,0,0],[0,0,1,1],[1,0,0,1],[0,1,0,1],[0,1,1,0],[1,0,1,0]]
    can_linked=[ [[],[],[],[]],
                 [[1,2,5,6],[1,2,4,7],[1,3,4,5],[1,3,6,7]],
                 [[1,2,5,6],[1,2,4,7],[],[]],
                 [[],[],[1,3,4,5],[1,3,6,7]],
                 [[1,2,5,6],[],[],[1,3,6,7]],
                 [[],[1,2,4,7],[],[1,3,6,7]],
                 [[],[1,2,4,7],[1,3,4,5],[]],
                 [[1,2,5,6],[],[1,3,4,5],[]]
                ]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    place=[]
    for _ in range(N):
        place.append(list(map(int,input().split())))

    checked=[(R,C)]
    queue=deque()
    queue.append((R,C,1))
    # l=1
    while queue:
        node = queue.popleft()
        r,c,l = node[0],node[1],node[2]
        if l==L:
            break
        # pt : pipe 종류번호
        pt = place[r][c]

        for i in range(4):
            if pipe_types[pt][i]==1:
                nr = r + dx[i]
                nc = c + dy[i]
                # 범위내에 있고
                if (0<=nr<N) and (0<=nc<M):
                    # 방문한 적 없고
                    if (nr,nc) not in checked:
                        # 파이프 연결 가능하다면
                        if (place[nr][nc] in can_linked[pt][i]) and place[nr][nc]:
                            queue.append((nr,nc,l+1))
                            checked.append((nr, nc))

    print(f"#{tc+1} {len(checked)}")
