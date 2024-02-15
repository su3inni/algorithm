def solution(users, emoticons):
    answer = [0,0]

    sale=[10,20,30,40]
    # 할인 경우의 수 모두 구하기 
    discount=[]
    
    # 조합구하기 
    def dfs(tmp,depth):
        if depth==len(emoticons):
            discount.append(tmp[:])
            return 
        for s in sale:
            tmp[depth]+=s 
            dfs(tmp,depth+1)
            tmp[depth]-=s 
    
    dfs([0]*len(emoticons),0)

    # 모든 조합 
    for d in range(len(discount)):
        plus_user = 0 
        profit = 0 
        # 사용자마다 확인
        for u in users:
            emoti_buy=0 
            for e in range(len(emoticons)):
                # 할인율 비교 
                if discount[d][e] >= u[0]:
                    emoti_buy += emoticons[e]*((100-discount[d][e])/100)
            # 기준 구매 비용 
            if emoti_buy >= u[1]:
                plus_user+=1 
            else:
                profit+=emoti_buy
        # 특정 할인율일때 업데이트된 값으로 정답 업데이트 여부 확인 
        if answer[0]<plus_user:
            answer = [plus_user,int(profit)]
        elif answer[0]==plus_user:
            if answer[1]<profit:
                answer = [plus_user,int(profit)]
    return answer
