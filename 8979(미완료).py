import sys
input = sys.stdin.readline

N, country = map(int,input().split())
lst = list(list(map(int, input().split())) for _ in range(N))
medal_dic = {}
for i in lst:
    medal_dic[i[0]] = i[1:]
    
# medal_dic = dict(sorted(medal_dic.items()))
medal_dic = sorted(medal_dic.items(),key=lambda item : (item[1][0],item[1][1],item[1][2]),reverse=True)
print(medal_dic)

prz = 1
cnt = 1
for i in range(1,N+1):
    if i != 1 :    
        if medal_dic[i-1] == medal_dic[i]:
            cnt += 1
        else: 
            prz += cnt
            cnt = 1
    if i == country :
        print(prz)
# print(medal_dic)