import sys

input = sys.stdin.readline
N = int(input()) 
comb = int(input())
cnct = []
virus = []

for c in range(comb):
    cnct.append(sorted(list(map(int,input().split()))))
cnct = sorted(cnct)
print(cnct)
if cnct[0][0] != 1 :
    print(0)
else :
    virus= cnct[0]
    lst = virus.copy()
    for c in cnct[1:]:
        print('virus : ',virus)
        print('c : ',c)
        lst += c
        print('lst : ',lst)
        if lst == list(set(lst)):        
            print('if : ',virus)
            print('-----')
            lst = virus.copy()
            
            
        elif len(lst) - len(list(set(lst))) ==1 :
            print('virus_2 : ',virus)
            virus.append(c[1])
            virus=sorted(virus)
            print('elif : ',virus)
            print('-----')
            lst = virus.copy()
            
        else : 
            print('else : ',virus)
            print('-----')
            lst = virus.copy()
            
            
        
    print(len(virus)-1)
    
    