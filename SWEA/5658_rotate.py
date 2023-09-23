T=int(input())

def slice_num(length):
    nums=[]
    idx_s,idx_e = 0,length
    for i in range(1,5):
        nums.append(arr[idx_s:idx_e])
        idx_s+=length
        idx_e+=length
    return nums

def rotate_arr(arr):
    record_num =arr[0]
    for i in range(1,n):
        next_num = arr[i]
        arr[i]=record_num
        record_num=next_num
    arr[0]=record_num

for tc in range(T):
    n,k = map(int,input().split())
    inp = input()

    arr=[]
    for i in range(n):
        arr.append(inp[i])

    # rotate 횟수
    r=n//4+1

    length=len(arr)//4

    answer_list=[]
    for i in range(r):
        nums = slice_num(length)
        rotate_arr(arr)

        for nn in nums:
            st=''
            for s in nn:
                st+=s
            # 16진수 to 10진수
            if int(st,16) not in answer_list:
                answer_list.append(int(st,16))

    answer_list.sort(reverse=True)
    print(f"#{tc+1} {answer_list[k-1]}")
