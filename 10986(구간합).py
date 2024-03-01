import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int,input().split())

#원본 배열
A = list(map(int,input().split()))

# 합배열
S = [0]* N

# 나머지 값이 같은 인덱스 수 저장하는 리스트
C = [0] * M

S[0] = A [0]

# 결과값 카운팅
cnt = 0

# 합 배열 만들기 
for i in range(1,N):
    S[i] = S[i-1] + A[i]


# 합 배열을 M으로 나눈 나머지 값으로 업데이트 
for i in range(N):
    remainder = S[i]%M
    S[i] = S[i]%M
    if remainder == 0 :
        cnt += 1
    C[remainder] += 1  #나머지 값이 같은 인덱스 개수 업데이트
    print(C)
print(S)
# 나머지 값이 같은 인덱스 중 2개를 뽑은 경우의 수 더하기    
for i in range(M):
    if C[i] > 1:
        cnt += (C[i]*(C[i]-1)//2) # 조합 공식 
    
# print(cnt)
