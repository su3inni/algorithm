def solution(record):
    answer = []
    check={}
    answer_pre=[]
    for r in record:
        try:
            stat,uid,nick = r.split(" ")
        except:
            stat,uid=r.split(" ")
        if stat=="Enter":
            check[uid] = nick
            answer_pre.append([uid,stat])
        elif stat == "Change":
            if uid in check.keys():
                check[uid]=nick 
        else:
            answer_pre.append([uid,stat])
    for a in answer_pre:
        if a[1]=="Leave":
            message = f"{check[a[0]]}님이 나갔습니다."
        elif a[1]=="Enter":
            message = f"{check[a[0]]}님이 들어왔습니다."
        answer.append(message)
    return answer
