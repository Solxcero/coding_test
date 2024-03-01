# 덩치
'''
(x,y) (p,q)
키, 몸무게 둘다 크면 덩치가 큰거임
나보다 덩치가 큰 사람의 수 = k
내 등수 = k+1
'''

import sys
input = sys.stdin.readline

N = int(input())

people = []

for _ in range(N):
    people.append(list(map(int,input().split())))
    
# print(people)
order = [1 for _ in range(N)]
# print(order)
for i in range(N-1):
    w = people[i][0]
    h = people[i][1]
    for j in range(i+1,N):
        if w > people[j][0] and h > people[j][1]:
            order[j] += 1
        elif w < people[j][0] and h < people[j][1]:
            order[i] += 1
for o in order:
    print(o,end=' ')