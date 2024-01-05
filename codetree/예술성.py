N = int(input())

art_map = [ list(map(int,input().split())) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def find_group(x,y,color,group):
    group.append([x,y])
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        if 0<=nx<N and 0<=ny<N:
            if visited[nx][ny]==0 and art_map[nx][ny]==color:
                visited[nx][ny]=1
                group = find_group(nx,ny,color,group)
    return group


def count_combi(M):
    combi=[]
    for i in range(M):
        for j in range(i+1,M):
            combi.append([i,j])
    return combi

def nearby(a,b):
    count=0
    for i in range(len(a)):
        target = a[i]
        for j in range(len(b)):
            if abs(target[0]-b[j][0])+abs(target[1]-b[j][1]) ==1 :
                count+=1
    return count

def calc_artscore(groups):
    total_score=0
    compare_group = count_combi(len(groups))
    for cg in compare_group:
        aidx = cg[0]
        bidx = cg[1]
        agroup = groups[aidx]
        bgroup = groups[bidx]
        # print("그룹",agroup,"&",bgroup)
        count = nearby(agroup[2],bgroup[2])
        # print("인접한 면의 갯수 :",count)
        score = (agroup[1]+bgroup[1])*agroup[0]*bgroup[0]*count
        total_score+=score
    return total_score

def rotate_cross():
    ret = [[0 for _ in range(N)] for _ in range(N)]
    for c in range(1, N // 2 + 1):
        sx = N // 2 - c
        sy = N // 2
        ret[sx + c][sy - c] = art_map[sx][sy]
        sx = sx + c
        sy = sy - c
        ret[sx + c][sy + c] = art_map[sx][sy]
        sx = sx + c
        sy = sy + c
        ret[sx - c][sy + c] = art_map[sx][sy]
        sx = sx - c
        sy = sy + c
        ret[sx - c][sy - c] = art_map[sx][sy]

    for i in range(N):
        for j in range(N):
            if ret[i][j]!=0:
                art_map[i][j]=ret[i][j]

def rotate(fractions,M):
    ret = [ [0 for _ in range(M)] for _ in range(M)]
    for i in range(M):
        for j in range(M):
            ret[j][M-1-i] = fractions[i][j]
    return ret

def cutting(rs,re,cs,ce):
    ret=[]
    fracs = art_map[rs:re]
    for f in fracs:
        ret.append(f[cs:ce])
    return ret

def change_board(retfrac,rr,rc):
    for i in range(N//2):
        for j in range(N//2):
           art_map[i+rr][j+rc] =  retfrac[i][j]

answer=0
for h in range(4):
    # 0. 그룹화하기
    color = 0
    visited=[[0 for _ in range(N)] for _ in range(N)]
    groups=[]
    for i in range(N):
        for j in range(N):
            # if art_map[i][j]!=color and visited[i][j]==0:
            if visited[i][j] == 0:
                visited[i][j]=1
                color=art_map[i][j]
                group = find_group(i,j,color,[])
                groups.append([art_map[i][j],len(group),group])

    print("그룹별")
    for g in groups:
        print(g)
    # 1. 예술점수 측정하기
    score = calc_artscore(groups)
    answer+=score
    print(f"{h}회차 ",score)

    # 2. 회전
    # 2-1. 중앙 회전
    print("중앙회전 전")
    for b in art_map:
        print(b)
    rotate_cross()
    print("중앙회전 후")
    for b in art_map:
        print(b)

    # 2-2. 나머지 회전
    frac1 = cutting(0,N//2,0,N//2)
    retfrac1 = rotate(frac1,N//2)
    change_board(retfrac1,0,0)


    frac2 = cutting(0,N//2,N//2+1,N)
    retfrac2 = rotate(frac2,N//2)
    change_board(retfrac2,0,N//2+1)

    frac3 = cutting(N//2+1,N,0,N//2)
    retfrac3 = rotate(frac3,N//2)
    change_board(retfrac3,N//2+1,0)


    frac4 = cutting(N//2+1,N,N//2+1,N)
    retfrac4 = rotate(frac4,N//2)
    change_board(retfrac4,N//2+1,N//2+1)

    print("부분회전 후")
    for b in art_map:
        print(b)

print(answer)
