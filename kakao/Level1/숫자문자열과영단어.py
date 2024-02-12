def solution(s):
    answer = ''
    part=''
    lang = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0'}
    for sp in s:
        if sp.isalpha():
            part+=sp
            if part in lang.keys():
                answer+=lang[part]
                part=''
                
        elif sp.isdigit():
            if part!='':
                answer+=lang[part]
                part=''
            answer+=str(sp) 
    if part!='':
        print(part)
    answer=int(answer)
    return answer
