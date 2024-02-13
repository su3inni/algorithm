def change(arr,n):
    check_board=[]
    for a in arr:
        binary_num = bin(a)[2:]
        bin_board=[]
        if len(binary_num)!=n:
            for i in range(n-len(binary_num)):
                bin_board.append(0)
            for b in binary_num:
                bin_board.append(b)
        else:
            for b in binary_num:
                bin_board.append(b)
        check_board.append(bin_board) 
    return check_board
    
def solution(n, arr1, arr2):
    answer = []
    a1board = change(arr1,n)
    a2board = change(arr2,n)
    for i in range(n):
        answer_str=''
        for j in range(n):
            if a1board[i][j]=='1' or a2board[i][j]=='1':
                answer_str+='#'
            else :
                answer_str+=' '
        answer.append(answer_str)
    return answer
