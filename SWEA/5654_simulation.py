T = int(input())


dx = [0,0,-0.5,0.5]
dy = [0.5,-0.5,0,0]

for tc in range(T):
    N = int(input())

    dots=[ list(map(int,input().split())) for _ in range(N)]

    power=0
    for i in range(4000):
        if len(dots)<2:
            break

        dots_dict={}
        for d in dots:
            nx = d[0]+dx[d[2]]
            ny = d[1]+dy[d[2]]
            if (nx,ny) in dots_dict:

                dots_dict[(nx,ny)].append([nx,ny,d[2],d[3]])
            else:
                dots_dict[(nx,ny)]=[[nx,ny,d[2],d[3]]]

        new_dots=[]
        # 이동 후
        for d in dots_dict:
            if len(dots_dict[d])==1:
                if -1000 <= dots_dict[d][0][0] <= 1000 and -1000<=dots_dict[d][0][1]<=1000:
                    new_dots.append(*dots_dict[d])
            else:
                for p in dots_dict[d]:
                    power+=p[3]

        dots=new_dots

    print(f"#{tc+1} {power}")

