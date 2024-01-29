M,T = map(int,input().split())
# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
mdx = [-1,-1,0,1,1,1,0,-1]
mdy = [0,-1,-1,-1,0,1,1,1]

pr,pc = map(int,input().split())
pr-=1
pc-=1

mon={}
for i in range(M):
    r,c,d = map(int,input().split())
    try:
        mon[(r-1,c-1)].append(d-1)
    except:
        mon[(r-1,c-1)]=[d-1]

def moncopy():
    init_mon = {}
    for m in mon:
        init_mon[m]=mon[m]
    return init_mon

def movemon():
    updatemon={}

    for m in mon :
        r,c = m[0],m[1]
        for md in mon[m]:
            nr = r + mdx[md]
            nc = c + mdy[md]
            if 0<=nr<4 and 0<=nc<4 and [nr,nc]!=[pr,pc] and (nr,nc) not in dead:
                try:
                    updatemon[(nr,nc)].append(md)
                except:
                    updatemon[(nr,nc)] = [md]
            else:
                change=False
                for d in range(8):
                    nmd = (md+1)%8
                    nr = r + mdx[nmd]
                    nc = c + mdy[nmd]
                    if 0 <= nr < 4 and 0 <= nc < 4 and [nr, nc] != [pr, pc] and (nr, nc) not in dead:
                        change=True
                        try:
                            updatemon[(nr, nc)].append(nmd)
                        except:
                            updatemon[(nr, nc)] = [nmd]
                        break
                    else:
                        md = nmd
                if change==False:
                    try:
                        updatemon[(r,c)].append(md)
                    except:
                        updatemon[(r,c)]=[md]
    return updatemon

# 우선순위 상좌하우
pdx=[-1,0,1,0]
pdy=[0,-1,0,1]
def findmax():

    s1,s2,s3=0,0,0
    max_kill = 0
    for d in range(4):
        visited = [[0 for _ in range(4)] for _ in range(4)]
        one_kill=0
        npr = pr + pdx[d]
        npc = pc + pdy[d]
        if 0<=npr<4 and 0<=npc<4:
            visited[pr][pc]=1
            if (npr,npc) in mon and visited[npr][npc]==0:
                one_kill = len(mon[(npr,npc)])
            for dd in range(4):
                second_kill=0
                nnpr = npr + pdx[dd]
                nnpc = npc + pdy[dd]
                if 0<=nnpr<4 and 0<=nnpc<4:
                    visited[npr][npc]=1
                    if (nnpr,nnpc) in mon and visited[nnpr][nnpc]==0:
                        second_kill =len(mon[(nnpr,nnpc)])
                    for ddd in range(4):
                        third_kill=0
                        nnnpr = nnpr + pdx[ddd]
                        nnnpc = nnpc + pdy[ddd]
                        if 0<=nnnpr<4 and 0<=nnnpc<4:
                            visited[nnpr][nnpc]=1
                            if (nnnpr,nnnpc) in mon and visited[nnnpr][nnnpc]==0:
                                third_kill =len(mon[(nnnpr,nnnpc)])

                            if max_kill<one_kill+second_kill+third_kill:
                                print(one_kill,second_kill,third_kill)
                                max_kill=one_kill+second_kill+third_kill
                                s1,s2,s3 = d,dd,ddd
    return s1,s2,s3,max_kill

def movepac(pr,pc):
    # 가장 많이 몬스터를 먹을 수 있는 경로 확인
    d1,d2,d3,killcnt = findmax()

    # 경로대로 움직이면서 시체 추가
    print("팩맨 먹은 방향",d1,d2,d3,"먹은 수",killcnt)
    pr = pr + pdx[d1]
    pc = pc + pdy[d1]
    if (pr,pc) in mon:
        del mon[(pr,pc)]
        dead[(pr,pc)] = 3
    pr = pr + pdx[d2]
    pc = pc + pdy[d2]
    if (pr,pc) in mon:
        del mon[(pr,pc)]
        dead[(pr,pc)]=3

    pr = pr + pdx[d3]
    pc = pc + pdy[d3]
    if (pr,pc) in mon:
        del mon[(pr,pc)]
        dead[(pr,pc)]=3

    return pr,pc

dead={}
turn=0
while turn<T:
    # 1. 알 생성
    initmon = moncopy()
    # 2. 몬스터 이동
    print("몬스터 이동 전: ",mon)
    mon = movemon()
    print("몬스터 이동 후: ",mon)
    # 3. 팩맨 이동
    print("팩맨 위치: ",pr,pc)
    pr,pc = movepac(pr,pc)
    print("팩맨 먹은 후: ",mon)
    print("팩맨 움직인 후: ",pr,pc)
    # 4. 몬스터 시체 관리
    deadlist = [ d for d in dead]
    for d in deadlist:
        if dead[d]>1:
            dead[d]-=1
        else:
            del dead[d]
    # 5. 알 > 몬스터
    for e in initmon:
        try:
            newmon = initmon[e]
            for nm in newmon:
                mon[e].append(nm)
        except:
            mon[e] = initmon[e]

    print("새로운 몬스터 생성 후 :", mon)
    print()
    turn+=1

answer=0
for m in mon:
    answer+=len(mon[m])

print(answer)
