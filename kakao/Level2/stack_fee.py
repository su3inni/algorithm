import math

def solution(fees, records):
    answer = []
    default_time , default_price, per_time, per_price = fees
    
    record_dict={}
    answer_dict={}
    for r in records:
        time, num, stat = r.split(" ")
        h,m = time.split(":")
        minute = int(h)*60 + int(m)
        num = int(num)
        if stat == "IN":
            record_dict[num]=minute
            
        elif stat == "OUT":
            if num in record_dict.keys():
                intime = record_dict[num]      
                # 채점이 틀렸던 이유 
                # IN - OUT , IN - OUT , IN 처럼 IN-OUT이 여러번 있었던 경우에 대한 처리 
                if num in answer_dict.keys():
                    answer_dict[num]+=minute-intime
                else:
                    answer_dict[num]=minute-intime
                    
                del record_dict[num]
    
    # IN 만 있는 경우 처리 
    for n in record_dict.keys():
        t = record_dict[n]
        add_time = (23*60+59) - t
        
        if n in answer_dict.keys():
            answer_dict[n]+=add_time
        else:
            answer_dict[n] = add_time
    
    # 차량번호 작은 것 부터 정렬
    sad = sorted(answer_dict.items(),key=lambda x:x[0])
    
    for n,t in sad:
        if t-default_time<=0:
            answer.append(default_price)
        else:
            fee = default_price + math.ceil((t-default_time)/per_time)*per_price
            answer.append(fee)
    
    return answer
