py,pm,pd = map(int,input().split())
ny,nm,nd = map(int,input().split())

# 만나이
man_age = 0
if ny!=py:
    checky=py
    while checky<ny-1 :
        man_age+=1
        checky+=1
    
    # 이 부분 틀렸던 부분 
    # if pm<=nm 으로 잘못 작성한 조건문으로, 달/일 처리 조심하자
    if pm < nm:
        man_age += 1
    elif pm == nm :
        if pd <= nd :
            man_age+=1

print(man_age)

# 세는 나이
calc_age = ny-py+1
print(calc_age)
# 연 나이
year_age = ny-py
print(year_age)
