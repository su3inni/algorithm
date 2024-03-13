T = int(input())

def check(pwd):
    left=[]
    right=[]
    for p in pwd:
        if p=='-':
            if left:
                left.pop()
        elif p=='<' :
            if left:
                move = left.pop()
                right.append(move)
        elif p=='>' :
            if right:
                move = right.pop()
                left.append(move)
        else:
            left.append(p)
    # left.extend(reversed(right))
    left += reversed(right)
    real = ''
    for r in left:
        real+=r

    return real

for _ in range(T):
    pwdstr = input()
    realpwd = check(pwdstr)
    print(realpwd)


# 시간초과
# T = int(input())
#
# def check(pwd):
#     chk = []
#     idx=-1
#     for c in pwd:
#         if c=='-' and idx!=-1:
#             chk.pop(idx)
#             idx-=1
#         elif c=='>' and len(chk)!=idx+1:
#             idx+=1
#         elif c=='<' and idx!=-1:
#             idx-=1
#         elif c.isalpha() or c.isdigit():
#             idx+=1
#             chk.insert(idx,c)
#     real=''
#     for c in chk:
#         real+=c
#     return real
#
# for _ in range(T):
#     pwdstr = input()
#     realpwd = check(pwdstr)
#     print(realpwd)
