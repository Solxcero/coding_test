# 셀프 넘버 ....
'''
n은  d(n)의 생성자 
생성자가 없는 수를 셀프넘버라고 함 ex) 1,3,5,7,9,20,31....
10,000보다 작거나 같은 셀프넘버 한 줄에 하나씩 증가하는 순서로 출력

첫번째 시도
1부터 10000까지 키값 갖는 딕셔너리 생성해서 
생성자를 갖는 수의 경우 1로 value 주고 셀프넘버는 0으로 

정답
set 자료형 이용 ! 차집합 개념을 사용하자 !!
'''

natural_num = set(range(1,10000+1))
generate_num = set()

for i in range(1,10000+1):
    for j in str(i):
        i += int(j)
    generate_num.add(i)

self_num = sorted(natural_num-generate_num)
for i in self_num:
    print(i)
    
    


    