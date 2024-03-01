import sys
input = sys.stdin.readline

N = int(input())

# 초기 변수 설정
cycle = 1 # 사이클 길이
new = 0 # 새로운 수
nn = N # 변화시킬 변수 

# 반복문으로 N과 new가 같아지는 시점까지 사이클 반복
while True :
    x = nn//10
    y = nn%10
    z = x+y
    new = (y*10) + (z%10)
    if N == new :
        print(cycle)
        break
    else:
        cycle += 1
        nn = new    
    
'''이거 안되는 이유 알아내야해... 
import sys
input = sys.stdin.readline

N = int(input())

# 초기 변수 설정
cycle = 0 # 사이클 길이
new = 0 # 새로운 수
nn = N # 변화시킬 변수 

# 반복문으로 N과 new가 같아지는 시점까지 사이클 반복
while N != new :
    x = nn//10
    y = nn%10
    z = x+y
    new = (y*10) + (z%10)
    cycle += 1
    nn = new

    
print(cycle)
'''