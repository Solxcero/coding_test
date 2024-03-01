# 그룹단어체커
import sys
input = sys.stdin.readline

N = int(input())
group = 0 # 그룹단어 갯수 카운트

for _ in range(N):
    word = str(input()).strip()
    
    check = [word[0]] # 첫번째 글자 미리 넣어 두기
    n = 0 
    # print(f'check : {check}')
    
    # 두번째 글자부터 비교하기
    for w in range(1,len(word)) :
        # check에 해당 알파벳이 없다면 , check 에 추가하기 
        if word[w] not in check :
            check.append(word[w])
            # print(f'if문 check : {check}')
            
        # check에 있다면 바로 앞 글자랑 비교해서 연속인지 확인하기
        else:
            if word[w-1] != word[w]:
                # print(f'{word[w]}가 연속하지 않는 곳에 존재 = group 조건 충족 실패')
                n += 1
                break
        # print(f'{word}는  그룹단어 입니다')
    if n == 0 :
        group += 1
print(group)
                
        
                
            
        