import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

lst.sort()
good = 0 
print(lst)
for i in range(N):
    # 합 확인할 정수 지정
    check = lst[i]
    print()
    print(f'[ check : {check} , i : {i} ]')
    s = 0 #시작 포인터
    e = N-1 #종료 포인터
    while s < e : 
        if lst[s] + lst[e] == check : 
            # print(f'check:{check} == now:{lst[s] + lst[e]} | s({s}), e({e})')
            print(f'sum:{lst[s] + lst[e]}  ({s},{e})', end= " → ")
            if s != i and e !=i:
                print(f'탈출 성공!!')
                good += 1
                break
            elif s == i : 
                print(f'탈출 실패 (s == i) : s ++')
                s+= 1
            elif e == i : 
                print(f'탈출 실패 (e == i) : e --')
                e -= 1    
        elif lst[s] + lst[e] < check : 
            # print(f'check:{check} > now:{lst[s] + lst[e]} | s({s}), e({e}) | s 이동')
            print(f'sum:{lst[s] + lst[e]}  ({s},{e})  s ++')
            s+=1
        else: 
            # print(f'check:{check} < now:{lst[s] + lst[e]} | s({s}), e({e}) | e 이동')
            print(f'sum:{lst[s] + lst[e]}  ({s},{e}) e --')
            e -= 1
print(good)