# 부녀회장이 될테야

'''
a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 
사람들을 데려와 살아야 함

비어있는 집 없음

k층의 n호에 몇명이 살고 있는지 출력
아파트는 0층부터 각층은 1호부터
0층의 i호에는 i명이 살고 있음

'''

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    apart = [i for i in range(1,n+1)]       
    for _ in range(k):
        for i in range(1,n):        
            apart[i] += apart[i-1]
        # print(apart)
    print(apart[-1])
    
    
# T = int(input())
# for _ in range(T):
#     k = int(input())
#     n = int(input())

#     apart = [[0 for _ in range(n)] for _ in range(k)]
#     for j in range(n):        
#         apart[0][j] = j+1
        
#     for i in range(1,len(apart)):
#         # print(f'---{i}층---')
#         for j in range(len(apart[i])):        
#             apart[i][j] = sum(apart[i-1][:j+1])
#             # print(f'{i}층 {j+1}호',end=' ')
#             # print(f'{apart[i][j]}명')
#     print(sum(apart[k-1][:n]))

            
            


    