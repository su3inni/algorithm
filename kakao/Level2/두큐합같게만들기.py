from collections import deque
def solution(queue1, queue2):
    answer = 0
    #list 의 pop(0)을 사용하면 시간 복잡도가 상승하기 때문에 
    #deque의 popleft()를 사용할 것

    queue1 = deque(queue1)
    queue2 = deque(queue2)
    q1sum = sum(queue1)
    q2sum = sum(queue2)
    if (q1sum + q2sum)%2!=0:
        return -1
    
    while True:
        if q1sum > q2sum:
            target = queue1.popleft()
            queue2.append(target)
            q1sum-=target
            q2sum+=target
            answer+=1
        elif q1sum < q2sum :
            target = queue2.popleft()
            queue1.append(target)
            q1sum+=target 
            q2sum-=target
            answer+=1 
        else:
            break
        
        if answer == len(queue1)*2:
            return -1
        
    
    
    return answer
