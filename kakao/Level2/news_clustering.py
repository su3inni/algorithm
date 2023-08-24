def split_str(string):
    str_list=[]
    for i in range(len(string)-1):
        if string[i].isalpha() and string[i+1].isalpha() :
            s=string[i]+string[i+1]
            str_list.append(s)
    return str_list

# 다중 교집합
def calc_interaction(l1,l2):
    inter=[]
    cpl2 = [ s.upper() for s in l2]

    for st in l1:
        if st.upper() in cpl2:
            inter.append(st)
            cpl2.pop(cpl2.index(st.upper()))
        else:
            continue
    return inter

def calc_union(l1,l2):
    union=[]
    cpl2 = [ s.upper() for s in l2]

    for st in l1:
        if st.upper() in cpl2:
            union.append(st)
            cpl2.pop(cpl2.index(st.upper()))
        else:
            union.append(st)
    
    for st in cpl2:
        union.append(st)
        
    return union
    

def solution(str1, str2):
    answer = 0
    str1_list=split_str(str1)
    str2_list=split_str(str2)

    interaction=calc_interaction(str1_list,str2_list)
    union=calc_union(str1_list,str2_list)
    
    if len(union)==0:
        return 65536
    
    answer=int((len(interaction)/len(union))*65536)
    
    return answer
