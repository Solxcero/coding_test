import sys
input = sys.stdin.readline

while True :
    a = str(input().strip())
    if a == '0':
        break
    half = a[:len(a)//2]
    if len(a) % 2 == 0 :
        oth = a[len(a)//2 :][::-1]
    else:
        oth = a[(len(a)//2) + 1:][::-1]
        
    if half == oth :
        print('yes')
    else:
        print('no')
    
    # a = int(input())
    # if a == 0:
    #     break
    # a = list(str(a))
    # half  = a[:len(a)//2]    
    # if len(a)%2 == 0 :
    #     oth = a[len(a)//2 :]
    # else:
    #     oth = a[(len(a)//2) + 1:]
    # print(f'half : {half}')
    # print(f'other : {oth}')
# print(lst)