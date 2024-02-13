def solution(new_id):
    answer = ''
    # step1 
    new_id = new_id.lower()
    # step2 
    process=''
    for n in new_id:
        if n.islower() or n.isdigit() or n in ['-','_','.']:
            process+=n
    #step3 
    step=''
    cum=''
    for n in process:
        if n=='.':
            cum+=n
        else:
            if cum!='':
                step+='.'
                cum=''
            step+=n

    # step4 
    if len(step)!=0:
        if step[0]=='.':
            if len(step)>=2:
                step = step[1:]
            else:
                step=''
    else:
        step='a'
    
    # step 6
    if len(step)>=16:
        step = step[:15]
        if step[14]=='.':
            step = step[:14]
    elif len(step)<=2:
        n = len(step)
        last = step[n-1]
        for i in range(3-n):
            step+=last
                    
    answer=step
    return answer
