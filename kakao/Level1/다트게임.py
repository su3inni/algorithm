def solution(dartResult):
    answer = 0
    score=[]
    digitflag=False
    for d in dartResult:
        if d.isnumeric():
            if digitflag:
                num = int(str(num)+d) 
            else:
                num = int(d)
            digitflag=True
        elif d in ['S','D','T']:
            digitflag=False
            if d == 'D':
                score.append(num**2)
            elif d=='T':
                score.append(num**3)
            else:
                score.append(num)
            
        elif d in ['*','#']:
            digitflag=False
            if d =='*':
                score[-1] = score[-1]*2
                try:
                    score[-2] = score[-2]*2
                except:
                    continue
            else:
                score[-1] = score[-1]*-1
    answer = sum(score)
    return answer
