from collections import deque
T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def sort_bricks(cur_bricks):
    for x in range(W):
        # 바닥부터 위로 확인
        prev = H - 1
        for y in range(H - 1, -1, -1):
            if cur_bricks[y][x]:
                if prev != y:
                    cur_bricks[prev][x], cur_bricks[y][x] = cur_bricks[y][x], cur_bricks[prev][x]
                # 빈 공간이라면 prev 는 유지하고 y값만 한 칸 줄어든다.
                # 때문에 이후 값들이 모두 연쇄적으로 switch될 것
                prev -= 1

def erase_blocks(y, x, cur_bricks):
    # queue = [(y,x,cur_bricks[y][x])]
    queue = deque()
    queue.append((y, x, cur_bricks[y][x]))

    # 너뭐냐
    cur_bricks[y][x] = 0
    erased_bricks = 1

    while queue:
        y, x, power = queue.popleft()

        # for p in range(1,power):
        #     for d in range(4):
        #         # 일단 여기가 다름
        #         ny, nx = y+p*dy[d] , x + p*dx[d]
        #         # 블록이라면
        #         if 0<=ny<H and 0<=nx<W and cur_bricks[ny][nx]!=0:
        #             queue.append((ny,nx,cur_bricks[ny][nx]))
        #             cur_bricks[ny][nx]=0
        #             erased_bricks += 1

        for d in range(4):
            oy, ox = y, x
            for p in range(power - 1):
                ny, nx = oy + dy[d], ox + dx[d]
                if 0 <= ny < H and 0 <= nx < W and cur_bricks[ny][nx] != 0:
                    queue.append((ny, nx, cur_bricks[ny][nx]))
                    cur_bricks[ny][nx] = 0
                    erased_bricks += 1
                oy, ox = ny, nx

    return erased_bricks

def dfs(result, k, bricks):
    global max_result
    if k == N:
        if max_result < result:
            max_result = result
        return

    for w in range(W):
        cur_bricks = [b[:] for b in bricks]
        cur_h = 0

        while cur_h < H and cur_bricks[cur_h][w] == 0:
            cur_h += 1

        num_erase = 0
        # cur_h가 H이면 그 줄은 비었다는 뜻이므로 부딪힐 벽돌이 없음
        if cur_h < H:
            num_erase = erase_blocks(cur_h, w, cur_bricks)
            sort_bricks(cur_bricks)


        dfs(result+num_erase , k+1 , cur_bricks)



for tc in range(T):
    N,W,H = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(H)]

    total_blocks=0
    for i in range(H):
        for j in range(W):
            if arr[i][j]>0:
                total_blocks+=1

    max_result=0
    dfs(0,0,arr)

    print(f"#{tc+1} {total_blocks-max_result}")
