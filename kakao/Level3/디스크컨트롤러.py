import heapq 
from collections import deque

def solution(jobs):
    jobs.sort()
    jobs = deque(jobs)
    num = len(jobs)
    waiting = []
    count = []
    time = 0 
    
    # 작업들이 count 배열에 들어갈거임
    while len(count)!=num:
        # 시작해야하는 작업들 waiting 큐에 넣기
        # 걸리는 시간이 0번째 요소로 들어감
        while jobs and time >= jobs[0][0]:
            top = jobs.popleft()
            heapq.heappush(waiting,(top[1],top[0]))
        
        if jobs and waiting==[]:
            top = jobs.popleft()
            time = top[0]
            heapq.heappush(waiting,(top[1],top[0]))
        
        # heap에서 가장 작은 요소가 앞에있는거임
        x,y = heapq.heappop(waiting)
        time+=x 
        # 걸린 시간 넣기
        count.append(time-y)
    
    answer = sum(count)//num
    return answer
