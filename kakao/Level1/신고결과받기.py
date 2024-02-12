def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    history = { }
    cnt={}
    ban_list=[]
    for id in id_list:
        history[id]=[]
        cnt[id]=0
    
    for rp in report:
        a = rp.split(' ')[0]
        b = rp.split(' ')[1]
        if b not in history[a]:
            history[a].append(b)
            cnt[b]+=1 
        if cnt[b]>=k:
            if b not in ban_list:
                ban_list.append(b)
                
    for bid in ban_list:
        for e,h in enumerate(history):
            if bid in history[h]:
                answer[e]+=1
        
    return answer
