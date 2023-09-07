def n_change(n,k):
    num=n
    st=''
    while num>0:
        mod=num%k
        st+=str(mod)
        num=num//k
    return st[::-1]

def check_prime(num):
    if num<2:
        return False
    elif num==2 or num==3:
        return True 
    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num%i==0:
                return False
    return True

    
def solution(n, k):
    answer = 0
    change_num = n_change(n,k)
    primecheck=change_num.split('0')
 
    for p in primecheck:
        if p!='' and check_prime(int(p)):
            answer+=1
    return answer
