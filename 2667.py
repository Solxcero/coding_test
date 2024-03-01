# 배열 크기 입력 -> 단지 정보 받기 
# 출력 1 : 단지 수 
# 출력 2 : 각 단지의 집 수 -> 오름차순

import sys
input = sys.stdin.readline

N = int(input())
map_ = list(list(map(int, input().rstrip())) for _ in range(N))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(map_, x, y):    
    stack = [(x,y)]
    map_[x][y] = 0
    count = 1
    while stack:
        x, y = stack.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
        
            if map_[nx][ny] == 1:
                stack.append((nx, ny))
                map_[nx][ny] = 0
                count += 1
                
    return count
    
result = []
for x in range(N):
    for y in range(N):
        if map_[x][y]==1:
            result.append(dfs(map_, x,y))
            
print(len(result))       
result.sort()
for i in result:
    print(i)
