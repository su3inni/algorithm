import math

def change(n,k):
    result=''
    while n>0:
        div = n//k
        mod = n%k 
        n = div 
        result+=str(mod)
    result = result[::-1]
    return result 

def solution(n, k):
    answer = 0
    changeresult = change(n,k)
    check = changeresult.split("0")
    
    check_prime = []
    for c in check:
        if c!='' and c!='1' :
            check_prime.append(int(c))
    
    # 약수 구하는 방식에서 시간 초과 줄이기
    for cp in check_prime:
        flag=True
        for i in range(2,int(math.sqrt(cp))+1):
            if cp%i==0:
                flag=False
                break 
        if flag:
            answer+=1
            
    return answer
