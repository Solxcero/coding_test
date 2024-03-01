import sys
input = sys.stdin.readline

N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int,input().split())))
    # cost+=(list(map(int,input().split())))
dp = [[0]*3 for _ in range(N)]
# print(cost)
# for i in range(N):
#     dp.append(min(cost[i]))
# print(dp)
dp[0] = cost[0]
print(dp[0])
for i in range(1,N):
    # R(임의로)
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + cost[i][2]
    print(dp[i])
print(min(dp[N-1]))
