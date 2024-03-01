# 남자 : 자기 수의 배수 상태 바꾸기 : 1
# 여자 : 자기 수 기준 좌우 대칭인 구간 전체 상태 바꿈 (좌우 대칭 아닌경우 자기 자신만 상태 바꿈) :  2
# 한 줄에 스위치 20개 씩만 출력 (줄바꿈 구현 포함)

import sys
input = sys.stdin.readline

N = int(input())
switch = list(map(int,input().split()))
std = int(input())

def onoff(s):
    if switch[s] == 0 :
        switch[s] = 1
    else :
        switch[s] = 0 
    return switch

def boy(b):
    i = b
    while i <= N :
        onoff(i-1)
        i += b
    return switch

def girl(b):
    i = b
    s = i-1
    e = i+1

    onoff(i-1)
    
    if e > N :
        return switch
    else:
        # 이거 조건 순서대로 확인한다.. 유레카.... 조건 순서 중요하다....
        while (s-1) >= 0 and (e-1) < N and switch[s-1] == switch[e-1] :
            onoff(s-1)
            onoff(e-1)
            s -= 1
            e += 1
        return switch

for _ in range(std):
    a,b = map(int,input().split())
    if a == 1:
        boy(b)
    else:
        girl(b)

for a in range(0,N,20):
    print(*switch[a:a+20])