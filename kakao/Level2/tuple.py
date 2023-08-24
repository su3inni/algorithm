def solution(s):
    answer = []
    
    s = s[2:-2]
    ts = s.split('},{')
    ts.sort(key=len)

    for t in ts:
        for i in t.split(','):
            if int(i) not in answer:
                answer.append(int(i))                

    return answer
