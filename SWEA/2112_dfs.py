D,W,K = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(D)]
def check_glass(arr):
    for i in range(W):
        prev=arr[D-1][i]
        cnt=1
        for d in range(D-2,0,-1):
            if prev==arr[d][i]:
                cnt+=1
            else:
                prev=arr[d][i]
            if cnt>=K :
                break
        if cnt < K :
            return False
    return True

def dfs(glass,f,mcnt):
    global answer,min_cnt
    if mcnt==K:
        return
    if check_glass(glass):
        if mcnt < min_cnt:
            min_cnt=mcnt
        return

    # A약품 칠하기
    for d in range(f,D):
        backup_r = []
        for w in range(W):
            if glass[d][w]==0:
                glass[d][w]=1
                backup_r.append(w)
        dfs(glass,d+1,mcnt+1)

        for w in backup_r:
            glass[d][w]=0

    # B 약품 칠하기
    for d in range(f,D):
        backup_r=[]
        for w in range(W):
            if glass[d][w]==1:
                glass[d][w]=0
                backup_r.append(w)
        dfs(glass,d+1,mcnt+1)

        for w in backup_r:
            glass[d][w]=1


answer=0
min_cnt=K
cparr = [ row[:] for row in arr]
dfs(cparr,0,0)
print(min_cnt)
