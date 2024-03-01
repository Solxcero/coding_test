import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lst = list(map(int,input().split()))
lst.sort() # 리스트 정렬

# 사용 변수들 초기화 
cnt  = 0  # 합이  M인 경우의 수 카운트
s = 0  # 시작 인덱스 지정
e = N-1 # 마지막 인덱스 지정

while s < e :
    if lst[s] + lst[e] == M : 
        print(f's:{s}({lst[s]}) e:{e}({lst[e]}) => 합이 {M}과 같음')        
        cnt += 1
        s += 1
        e -= 1
    elif lst[s] + lst[e] < M :
        print(f's:{s}({lst[s]}) e:{e}({lst[e]}) => 합이 {M} 보다 작음')        
        s += 1
    else:
        print(f's:{s}({lst[s]}) e:{e}({lst[e]}) => 합이 {M} 보다 큼')        
        e -=1
print(cnt)
        

