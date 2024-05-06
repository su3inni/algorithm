def solution(players, callings):
    answer = []
    name={}
    info={}
    for idx,p in enumerate(players):
        name[p]=idx+1
        info[idx+1]=p 
    

    for c in callings : 
        current_position = name[c]
        prev_position = current_position-1 
        
        prev_players = info[prev_position]
        
        name[prev_players]=current_position 
        name[c]=prev_position
        info[current_position] = prev_players
        info[prev_position] = c
        

    
    for p in info:
        answer.append(info[p])
    return answer
