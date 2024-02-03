def solution(today, terms, privacies):
    answer = []
    # 개인정보 N개, 약관종류 3개:유효기간 다름
    # 모든 달은 28일까지 있음
    # 오늘 날짜, 개인정보 수집날짜, 약관종류 
    
    #1. 개인정보 수집날짜와 약관종류에 따라 종료 날짜 리턴 
    #2. 종료날짜와 오늘날짜비교 
    ty,tm,td = map(int,today.split("."))
    tms = {}
    for t in terms:
        ts = t.split(' ')
        tms[ts[0]]=int(ts[1])
    
    for i,pvs in enumerate(privacies):
        info = pvs.split(" ")
        date,tpvs = info[0],info[1]
        ttpvs = tms[tpvs]
        gy,gm,gd = map(int,date.split("."))
        
        add_date = ttpvs*28
        add_date-=1
        gd+=add_date
        add_month = gd//28
        gd = gd%28
        if gd==0:
            add_month-=1
            gd=28
        
        gm+=add_month
        add_year = gm//12 
        gm = gm%12 
        if gm==0:
            add_year-=1
            gm=12
        
        gy +=add_year 
        
        # print(gy,gm,gd)
        # 년도가 다를때
        if ty>gy:
            answer.append(i+1)
        # 년도가 같을 때
        elif ty==gy:
            if tm>gm:
                answer.append(i+1)
            elif tm==gm:
                if td>gd:
                    answer.append(i+1)
        
    answer.sort()
    
    return answer
