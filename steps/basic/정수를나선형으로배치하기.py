def solution(n):
    # n의 범위를 잘 보고 코드 작성하기 : 이 부분 때문에 런타임 에러
    if n==1:
        return [[1]]
    
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    x,y = 0,0 
    direction = 0 
    
    for i in range(n*n):
        answer[x][y]=i+1 
        if direction==0:
            y+=1 
            if y==n-1 or answer[x][y+1]!=0:
                direction = 1
        elif direction==1:
            x+=1 
            if x==n-1 or answer[x+1][y]!=0:
                direction=2 
        elif direction == 2: 
            y-=1 
            if y==0 or answer[x][y-1]!=0:
                direction=3 
        elif direction==3:
            x-=1
            if x==0 or answer[x-1][y]!=0:
                direction=0
        
    return answer
