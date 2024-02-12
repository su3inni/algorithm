def solution(survey, choices):
    answer = ''
    cnt = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for idx,t in enumerate(survey):
        da = t[0]
        a = t[1]
        if 1<=choices[idx]<=3:
            cnt[da]+=(4-choices[idx])
        elif 5<=choices[idx]<=7:
            cnt[a]+=(choices[idx]-4)
            
    pair = [['R','T'],['C','F'],['J','M'],['A','N']]
    for p in pair : 
        f = p[0]
        s = p[1] 
        if cnt[f]<cnt[s]:
            answer+=s 
        else:
            answer+=f
    return answer
