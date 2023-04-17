"""
sum=0 # ★sum=0으로 초기화해주는거 개중요
i=1
while(i<11):
    sum=sum+i
    print(sum)
    i=i+1
"""
 #5의 배수의 합계 구하기   
sum=0
i=100

while i<=300:
    if i%5==0:
        sum=sum+i # ==> sum+=i
    i=i+1#이건 하나 증가시켜서 다시 while로 올려주는 역할

print(sum)
print("\n")
"""
8200

"""

"""
무한루프 중지하는법 cntrol+c

while True:
    print('c')
이게무한루프임
"""

#1 회 실행합니다 . break 때문에 딱 1회만 실행
for i in range(1,1001,1):
    print(i,"회 실행합니다")
    break
print("\n")
"""
1 회 실행합니다
"""


#1에서부터 10까지 더하는데 i와 sum을 표시해주는 프로그램
i = 1
sum = 0
while True:
    if i > 10:
        break
    print('i', '=', i, 'sum', '=', sum)
    sum = sum+i
    i = i+1
print("합계", sum)
print("\n")
"""
i = 1 sum = 0
i = 2 sum = 1
i = 3 sum = 3
i = 4 sum = 6
i = 5 sum = 10
i = 6 sum = 15
i = 7 sum = 21
i = 8 sum = 28
i = 9 sum = 36
i = 10 sum = 45
합계 55
"""
#1~100를 더하되 4의 배수는 더하지 않는 프로그램
i=0
hap=0
for i in range(1,101,1):
    if i%4==0:
        continue
    hap=i+hap
print("합계는",hap)
print("\n")
"""
합계는 3750
"""
#주사위 3개를 동시에 던져 동일한 숫자 나오기/얼마나 나왔는지 세기
import random #★★ 랜덤값 구할땐 import random 선언해주는거 개중요!!!!!!!!!!

count=0
dice1,dice2,dice3=0,0,0
while True:
    count=count+1
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice3=random.randint(1,6)
    if (dice1==dice2)and(dice2==dice3):
        break
print("3개 주사위는 모두",dice1,"입니다.")
print("이것이 나오기까지",count,"번 던졌습니다.")

import random
count=0
d1,d2,d3=0,0,0
while True:
    count=count+1
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    d3=random.randint(1,6)
    if (d1==d2)and(d2==d3):
        break
print(count,"번 던졌고","숫자는",d1,"입니다")
print("\n")
"""
3개 주사위는 모두 1 입니다.
이것이 나오기까지 116 번 던졌습니다.
69 번 던졌고 숫자는 1 입니다
"""

#컴퓨터와 인간의 숫자 맞히기 대결(랜덤)+몇회 돌렸는지도 출력
import random

computer=0
human=0
for i in range(1,11,1):
    coumputer=random.randint(1,5)
    print("게임",i,"회 돌림."," ")
    human=int(input("컴퓨터가 생각한 숫자는 무엇일까? :"))
    if computer==human:
        print("맞음 ㅊㅋ")
        break
    else:
        print("틀림. 다시 ㄱㄱ: ")
        continue
print("게임끝")
"""

게임 1 회 돌림.  
컴퓨터가 생각한 숫자는 무엇일까? :0
맞음 ㅊㅋ
게임끝
or
게임 1 회 돌림.  
컴퓨터가 생각한 숫자는 무엇일까? :9
틀림. 다시 ㄱㄱ: 
게임 2 회 돌림.  
컴퓨터가 생각한 숫자는 무엇일까? :3
틀림. 다시 ㄱㄱ: 
게임 3 회 돌림.  
컴퓨터가 생각한 숫자는 무엇일까? :4
틀림. 다시 ㄱㄱ: 
게임 4 회 돌림.  
컴퓨터가 생각한 숫자는 무엇일까? :
"""
