def solution(N, stages):
    answer = []
    fail=[[0,_] for _ in range(N)]
    people = len(stages)
    
    for i in range(1,N+1):
        stage_go=0
        stage_stay=0
        for s in stages:
            if s >= i :
                stage_go+=1 
            if s==i:
                stage_stay+=1
        if stage_go!=0:
            fail[i-1][0]=stage_stay/stage_go
    
    fail.sort(reverse=True,key=lambda x:x[0])
    for f in fail:
        answer.append(f[1]+1)
    return answer
