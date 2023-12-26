from collections import deque

yellow = deque([0,0,0,0] for _ in range(6))
red = deque([0,0,0,0] for _ in range(6))

def reposition(t,x,y):
    if t==1:
        # yellow, red
        return [[1,y]],[[1,x]]
    elif t==2:
        return [[1,y],[1,y+1]], [[0,x],[1,x]]
    elif t==3:
        return [[0,y],[1,y]], [[1,x],[1,x+1]]

def down(color,blocks):
    # 한개나 두개
    while True :
        for x,y in blocks:
            if x+1>5 or color[x+1][y]==1:
                for x,y in blocks:
                    color[x][y]=1
                # return 위치 잘보기
                return
        for i in range(len(blocks)):
                blocks[i][0]+=1

def check_score(color):
    score=0
    for i in range(2,6):
        if sum(color[i])==4:
            del color[i]
            color.appendleft([0,0,0,0])
            score+=1

    # 연한 칸에 있는 경우 밀어내기
    while 1 in color[1]:
        color.pop()
        color.appendleft([0,0,0,0])

    return score

def sum_blocks(color):
    sumblocks=0
    for i in range(2,6):
        sumblocks+=sum(color[i])
    return sumblocks

K = int(input())
answer_score=0
answer_left=0

for _ in range(K):
    t,x,y = map(int,input().split())
    yellow_blocks, red_blocks = reposition(t,x,y)

    down(yellow,yellow_blocks)
    down(red,red_blocks)
    answer_score+= check_score(yellow)
    answer_score+= check_score(red)

answer_left+=sum_blocks(yellow)
answer_left+=sum_blocks(red)

print(answer_score)
print(answer_left)