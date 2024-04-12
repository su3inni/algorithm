N,M = map(int,input().split())

arr=[]
for _ in range(N):
    rw = list(map(int,input().split()))
    arr.append(rw)

tr,tc = N//2,N//2
# 우 하 좌 상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 안에서 바깥으로
def check_map(N):
    dmap = [ [-1 for _ in range(N)] for _ in range(N)]
    sr,sc = N//2,N//2
    dr= 2
    dmap[sr][sc]=dr

    cnt=0
    check=1
    while check<N:
        for i in range(check):
            dmap[sr][sc]=dr
            sr,sc = sr+dx[dr],sc+dy[dr]
        dr = (dr - 1 + 4) % 4
        cnt+=1

        if check==N-1:
            if cnt==3:
                cnt=0
                check+=1
        else:
            if cnt==2:
                cnt=0
                check+=1



    return dmap

pull_map = check_map(N)

for pm in pull_map:
    print(pm)

def find_dup():
    i,j = N//2,N//2
    hist = []
    curr = arr[i][j]

    cum=[[i,j]]
    while 1:
        dr = pull_map[i][j]
        ni = i + dx[dr]
        nj = j + dy[dr]

        if not(0<=ni<N) or not(0<=nj<N):
            return hist

        if arr[ni][nj]==curr:
            cum.append([ni,nj])
        else:
            if len(cum)>=4:
                hist.append([curr,cum])

            cum=[[ni,nj]]
            curr = arr[ni][nj]

        i,j = ni,nj

    return hist

def rearrange():
    sr,sc = N//2,N//2

    while 1:
        curr = arr[sr][sc]
        if (sr,sc)==(0,0):
            break

        # 0 인 경우는 다음값과 swap
        dr = pull_map[sr][sc]
        if curr==0 and (sr,sc)!=(N//2,N//2):
            # 다음에 값이 있음
            nsr,nsc = sr+dx[dr],sc+dy[dr]
            # 다음 값이 존재하면
            if arr[nsr][nsc]!=0:
                arr[sr][sc], arr[nsr][nsc] = arr[nsr][nsc], arr[sr][sc]
                sr,sc = nsr,nsc
            # 다음 값도 0이면, 0이 아닌 부분이 나올 때 까지 탐색
            else:
                csr,csc = sr,sc
                cdr = dr
                while arr[csr][csc]==0 :
                    csr,csc = csr+dx[cdr],csc+dy[cdr]
                    if not(0<=csr<N) or not(0<=csc<N):
                        return
                    cdr = pull_map[csr][csc]

                arr[sr][sc], arr[csr][csc] = arr[csr][csc], arr[sr][sc]
            # print("MMMOVE")
            # for a in arr:
            #     print(a)
            # print()
        # 0이 아니라면 아니라면 다음 칸으로 이동
        else:
            sr,sc = sr+dx[dr],sc+dy[dr]


def add_score():
    score=0
    while 1:
        # 비어있는 공간만큼 채우기
        rearrange()
        print("재배열 후")
        for a in arr:
            print(a)

        # 같은 종류 4번 이상 중복되는지 찾기
        hist = find_dup()

        if len(hist)==0:
            return score
        else:
            for mtyp,h in hist:
                score+=len(h)*mtyp
                for r,c in h:
                    arr[r][c]=0


    return score

def get_list():
    gl=[]
    sr,sc = N//2,N//2

    while 1:
        dr = pull_map[sr][sc]
        sr,sc = sr+dx[dr], sc+dy[dr]
        if 0<=sr<N and 0<=sc<N and arr[sr][sc]!=0:
            gl.append(arr[sr][sc])
        else:
            return gl

    return gl


def make_arr(onearr):
    new = []
    cnt=1
    prev=onearr[0]
    for oa in onearr[1:]:
        if oa==prev:
            cnt+=1
        else:
            new.append(cnt)
            new.append(prev)
            cnt=1
            prev=oa

    new.append(cnt)
    new.append(prev)

    newarr = [ [0 for _ in range(N)] for _ in range(N)]
    sr,sc = N//2,N//2
    for a in new:
        dr = pull_map[sr][sc]
        sr,sc = sr+dx[dr],sc+dy[dr]
        if 0<=sr<N and 0<=sc<N:
            newarr[sr][sc]=a
        else:
            print(sr,sc)
            break

    return newarr


answer=0
for m in range(M):
    d,p = map(int,input().split())

    # [1] 공격 수 만큼 공격
    for i in range(1,p+1):
        nr = tr + dx[d]*i
        nc = tc + dy[d]*i
        if 0<=nr<N and 0<=nc<N:
            if arr[nr][nc]!=0:
                answer+=arr[nr][nc]
                arr[nr][nc]=0
    print()
    for a in arr:
        print(a)
    print()
    # [2] 비어 있는 공간만큼 채우기
    score = add_score()
    answer+=score

    # [3] 몬스터를 같은 숫자끼리 짝지음 ..
    onearr = get_list()
    print(onearr)
    arr = make_arr(onearr)
    print()
    for a in arr:
        print(a)
    print()
print(answer)
