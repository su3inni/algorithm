def solution(edges):
    answer = []
    node_dict = {}
    for e in edges:
        start = e[0]
        end = e[1]
        if start not in node_dict:
            node_dict[start] = [0,0]
        if end not in node_dict:
            node_dict[end] = [0,0]
        node_dict[start][0]+=1 
        node_dict[end][1]+=1 
    
    key_node = 0
    stick=0
    eight=0
    # 나가는거, 들어오는거
    for n in node_dict:
        if node_dict[n][0]>=2 and node_dict[n][1]==0:
            key_node = n
        elif node_dict[n][0] == 0 and node_dict[n][1]>0:
            stick+=1
        elif node_dict[n][0]==2 and node_dict[n][1]>=2:
            eight+=1 
    # print(node_dict)
    total_node = node_dict[key_node][0]
    donut = total_node-stick-eight
    
    answer = [key_node,donut,stick,eight]
            
    return answer
