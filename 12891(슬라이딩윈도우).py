import sys
input = sys.stdin.readline

S,P = map(int,input().split())
dna = input().rstrip()
a, c, g, t = map(int,input().split())

start = dna[:P]

temp = {'A':0,'C':0,'G':0,'T':0}

for i in start :
    temp[i] += 1

cnt = 0 
if temp['A'] >= a and temp['C'] >= c and temp['G'] >= g and temp['T'] >= t :
    cnt += 1

start_idx = 0 
end_idx = start_idx + P

for i in range(len(dna)-P):
    temp[dna[start_idx+i]] -= 1
    temp[dna[end_idx+i]] += 1
    if temp['A'] >= a and temp['C'] >= c and temp['G'] >= g and temp['T'] >= t :
        cnt += 1
        
print(cnt)