def solution(board, moves):
    answer = 0
    basket=[]
    N = len(board[0])
    
    for m in moves:
        m-=1
        pick=0
        for i in range(N):
            if board[i][m]!=0:
                pick=board[i][m]
                board[i][m]=0
                break 
        if pick==0:
            continue
        if len(basket)!=0:         
            if basket[len(basket)-1]==pick:
                answer+=2 
                basket.pop()
            else:
                basket.append(pick)
        else:
            basket.append(pick)
        
        # for b in board:
        #     print(b)
        # print(basket)
        # print()
        
    
    return answer
