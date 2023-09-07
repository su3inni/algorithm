def solution(msg):
    answer = []
    # 1. 사전 초기화     
    D = {chr(i) : i-64 for i in range(65,91)}

    start,end=0,1
    
    while end<len(msg):
        message=msg[start:end+1]
        # 사전에 추가
        if not message in list(D.keys()):
            D[message]=len(D)+1
            answer.append(D[message[:-1]])
            start=end
            end=start+1
        #사전에 있으면 가장 긴 수열 찾기 위해 +1 
        else:
            end+=1
    
    if msg[start:end] in list(D.keys()):
        answer.append(D[msg[start:end]])
    
    return answer
