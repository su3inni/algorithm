T=int(input())

for t in range(T):
    M, A = map(int, input().split())

    userA = list(map(int, input().split()))
    userB = list(map(int, input().split()))

    bc = []
    for i in range(A):
        bc.append((i, list(map(int, input().split()))))
    # X, 상, 우, 하, 좌
    dx = [0, 0, 1, 0, -1]
    dy = [0, -1, 0, 1, 0]

    ax, ay = 1, 1
    bx, by = 10, 10

    userA_info = []
    userB_info = []

    for i in range(0, M):
        userA_can = []
        userB_can = []
        for n, b in bc:
            # battery 범위 내에 있는지 확인
            # userA 확인
            if abs(ax - b[0]) + abs(ay - b[1]) <= b[2]:
                userA_can.append((n, b[3]))
            if abs(bx - b[0]) + abs(by - b[1]) <= b[2]:
                userB_can.append((n, b[3]))

        userA_info.append((ax, ay, i, sorted(userA_can, key=lambda x: x[1], reverse=True)))
        userB_info.append((bx, by, i, sorted(userB_can, key=lambda x: x[1], reverse=True)))

        direction_a = userA[i]
        ax += dx[direction_a]
        ay += dy[direction_a]

        direction_b = userB[i]
        bx += dx[direction_b]
        by += dy[direction_b]

    userA_can_last = []
    userB_can_last = []
    for n, b in bc:
        if abs(ax - b[0]) + abs(ay - b[1]) <= b[2]:
            userA_can_last.append((n, b[3]))
        if abs(bx - b[0]) + abs(by - b[1]) <= b[2]:
            userB_can_last.append((n, b[3]))
    userA_info.append((ax, ay, M, sorted(userA_can_last, key=lambda x: x[1], reverse=True)))
    userB_info.append((bx, by, M, sorted(userB_can_last, key=lambda x: x[1], reverse=True)))

    answer = 0
    # 배터리 최댓값 계산
    for i in range(M + 1):
        ab_list = userA_info[i][3]
        bb_list = userB_info[i][3]
        if len(ab_list) == 0 and len(bb_list) == 0:
            continue
        elif len(ab_list) == 0 and len(bb_list) != 0:
            answer += bb_list[0][1]
        elif len(bb_list) == 0 and len(ab_list) != 0:
            answer += ab_list[0][1]
        else:
            # 같은 타이밍에 최대 충전 가능한 양이 다를 경우
            if ab_list[0][1] != bb_list[0][1]:
                answer += (ab_list[0][1] + bb_list[0][1])
            # 같은 타이밍에 최대 충전 가능한 양이 같을 경우
            # 서로 다른 BC가 P가 같을 수 있음!!!
            elif (ab_list[0][1] == bb_list[0][1]) and (ab_list[0][0] != bb_list[0][0]):
                answer += ab_list[0][1]
                answer += bb_list[0][1]
            else:
                # 둘다 second 선택지 있는 경우
                if len(ab_list) > 1 and len(bb_list) > 1:
                    max_charge = max(ab_list[1][1], bb_list[1][1])
                    default_charge = ab_list[0][1]
                # A에만 second 선택지가 있을 경우
                elif len(ab_list) > 1:
                    max_charge = ab_list[1][1]
                    default_charge = bb_list[0][1]
                # B에만 second 선택지가 있을 경우
                elif len(bb_list) > 1:
                    max_charge = bb_list[1][1]
                    default_charge = ab_list[0][1]
                # second 선택지가 없는 경우
                else:
                    default_charge = ab_list[0][1]
                    max_charge = 0
                answer += (default_charge + max_charge)
    print(f"#{t+1} {answer}")
