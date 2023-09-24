T = int(input())


# 하나의 배열 내에서 경사로 설치 혹은 활주로 설치 가능한지 체크
def check(arr):
    cnt=1
    height=arr[0]
    install=[0 for _ in range(len(arr))]
    keep = False
    for i in range(1,n):
        # 높이가 2이상 차이나는 경우 경사로 X
        if abs(arr[i]-height)>=2:
            return False
        # 경사 차이가 없는 경우
        if height == arr[i]:
            cnt+=1
            if cnt == x and keep :
                install[i]=1
                keep=False
                cnt=0

        # 경사 차이가 1인 경우
        else:
            # 우측 높이가 더 큰 경우
            if height < arr[i]:
                # 경사로 길이가 되고, 중복 경사로 설치가 아닌 경우
                if cnt >= x and install[i-1]==0:
                    install[i-1]=1
                    height=arr[i]
                    cnt=1
                else:
                    return False
            # 좌측 높이가 더 큰 경우
            elif height > arr[i]:
                if keep and cnt >=x :
                    install[i-1]=1
                    keep=False
                    height=arr[i]
                elif keep and cnt<x :
                    return False
                else:
                    keep=True
                    cnt=1
                    height=arr[i]

    if keep and cnt<x:
        return False

    return True

for tc in range(T):
    n,x = map(int,input().split())

    height_map = [ list(map(int,input().split())) for _ in range(n)]

    answer=0
    # 가로
    for i in range(n):
        if check(height_map[i][:]) :
            # print("가로",height_map[i][:])
            answer+=1
    # 세로
    for i in range(n):
        varr=[]
        for j in range(n):
            varr.append(height_map[j][i])
        if check(varr) :
            # print("세로",varr)
            answer+=1

    print(f"#{tc+1} {answer}")
