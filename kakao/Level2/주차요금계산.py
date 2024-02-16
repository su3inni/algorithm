def calc_time(intime, outtime):
    inhour, inminite = intime.split(":")[0], intime.split(":")[1]
    outhour, outminite = outtime.split(":")[0], outtime.split(":")[1]
    if outminite == '00':
        outminite = '60'
    hours = int(outhour) - int(inhour)
    minite = int(outminite) - int(inminite)
    if outminite == "60":
        hours -= 1

    total_time = hours * 60 + minite
    return total_time


def checkout(totaltime, time, fee, pertime, perfee):
    totalfee = 0
    if totaltime > time:
        # multime = totaltime // time
        # totaltime -= (time * multime)
        # totalfee += (fee * multime)
        totaltime-=time
        totalfee+=fee
        if totaltime > 0:
            if totaltime % pertime == 0:
                totalfee += (totaltime // pertime) * perfee
            else:
                totalfee += ((totaltime // pertime) + 1) * perfee
    else:
        totalfee = fee
    return totalfee


def solution(fees, records):
    answer = []
    time, fee, per_time, per_fee = fees[0], fees[1], fees[2], fees[3]

    cars_records = {}
    for rc in records:
        rsplit = rc.split(' ')
        ctime, car, inout = rsplit[0], rsplit[1], rsplit[2]
        if car not in cars_records:
            if inout == 'IN':
                cars_records[car] = [ctime, 0, 0]
        elif car in cars_records:
            if inout == "OUT":
                intime, outtime, totaltime = cars_records[car]
                addtime = calc_time(intime, ctime)
                totaltime += addtime
                cars_records[car] = [0, 0, totaltime]
            else:
                cars_records[car][0] = ctime

    answer_check = []
    for cr in cars_records:
        # 모두 출차됨 정산하기
        if cars_records[cr][0] == 0 and cars_records[cr][1] == 0:
            totaltime = cars_records[cr][2]
            totalfee = checkout(totaltime, time, fee, per_time, per_fee)
            answer_check.append([int(cr), totalfee])
        else:
            addtime = calc_time(cars_records[cr][0], "23:59")
            totaltime = cars_records[cr][2]
            totaltime += addtime
            totalfee = checkout(totaltime, time, fee, per_time, per_fee)

            answer_check.append([int(cr), totalfee])

    answer_check.sort()
    answer = [ a[1] for a in answer_check ] 
    return answer
