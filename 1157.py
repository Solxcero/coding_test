s = input().upper()
words = {}
for c in s:
	if c not in words:
		words[c] = 1
	else:
		words[c] += 1

arr = [c for c, v in words.items() if v == max(words.values())]

if len(arr) > 1:
	print('?')
else:
	print(arr[0])

'''
import sys
input = sys.stdin.readline

s = str(input()).strip()
s = s.upper()

cnt = {}
for i in s:
    if i not in cnt :
        cnt[i]  = 1
    else:
        cnt[i] += 1
 
res = sorted(list(cnt.items()),key=lambda x:x[1],reverse=True)

if len(res) >1 :
    if res[0][1] == res[1][1]: # 글자수 자체가 1개일 수도 있으니..!!!
        print('?')
    else:
        print(res[0][0])
else:
    print(res[0][0])
    '''

'''시간초과 풀이 -> 해결 !! 딕셔너리 길이가 1인 경우도 고려해주니 에러 안남!! count 문제가 아니었음 
cnt = []
lst = list(set(s))

for i in lst :
    cnt.append((i,s.count(i)))
    
cnt = sorted(cnt,key=lambda x : x[1],reverse=True)

# print(cnt)


if len(res) > 1:
    if cnt[0][1] == cnt[1][1]:
        print('?')
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
'''

    
    


