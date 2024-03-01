# 요세푸스
'''
1번부터 N번까지 원으로 앉음
K번째 사람 제거
N명 모두 제거 될때 까지 진행
제거 순서 출력


1 2 3 4 5 6 7  3
1 2 4 5 6 7    6
1 2 4 5 7      2
1 4 5 7        7
1 4 5          5
1 4            1
4              4

7 4

1 2 3 4 5 6 7  4
1 2 3 5 6 7    1
2 3 5 6 7      6
2 3 5 7        5
2 3 7          7
2 3            3
2              2
'''

N, K =map(int, input().split())

one = list(range(1,N+1))

i = 0 

print('<',end='')
while True : 
    i = (i+K-1)%len(one)
    print(one[i],end='')
    del one[i]
    if len(one) == 0 :
        break
    print(', ',end='')
print('>')

# 링크드 리스트 ..?
# rm = []
# while len(one)>0 : 
#     # print(one)
#     if len(one) < K : 
#         if len(one)== 1:
#             rm.append(one[0])
#             break
#         rm.append(one[(K//len(one))-1])
#         one = one[(K//len(one)):] + one[0:(K//len(one))-1]
#     else : 
#         rm.append(one[K-1])
#         one = one[K:] + one[0:K-1]    
    
# print('<',end='')
# for i in range(N) :
#     if i == N-1:
#         print(f'{rm[i]}>') 
#     else:
#         print(rm[i],end=', ')
