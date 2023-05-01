num=[10,20,30,40,50,60,70]
print(num[0])
print(num[-1])
print(num[::2]) # 처음부터 끝까지 다 출력하는건데 2칸식 건너뛰고출력하는거
print(num[1:3])

"""
10
70
[10, 30, 50, 70]
[20, 30]
"""
num2=[1,2,5]
num2[1:2]=[3,4] #1번부터 2번자리에3,4를 넣는것
print(num2)
"""
[1, 3, 4, 5]
"""
num2[4:5]=[6,7,8,9]
print(num2)
"""
[1, 3, 4, 5, 6, 7, 8, 9]
"""
#append(추가하려는 값) : 맨 뒤에 값 추가하기
#insert(추가하려는 위치,값) : 정해진 위치에 값 삽입

num=[10,20,30]
num.insert(1,123) #1번자리에 123 삽입
print(num)
"""
[10, 123, 20, 30]
"""
#del(num[삭제하고 싶은 함수의 번호]) : 리스트의 항목 삭제
num=[10,20,30]
del(num[1])
print(num)
"""[10, 30]"""

#remove(지울 값) : 리스트에서 특정 값 삭제
num=[10,20,30]
num.remove(10) #리스트에서 10을 지우라는 뜻
print(num)

num=[10,10,10,20,30] #10이 3개나..?!
num.remove(10) #리스트에서 10을 지우라는 뜻, 근데 10이 많으면 전부 다 지워지는게 아니라 한개만 지워짐!
print(num)
"""
[10, 10, 20, 30]
"""
#pop() 제일 뒤의 값을 뽑아내서 값을 알려준 뒤 삭제
num=[10,20,30]
num.pop()
print(num)
"""[10, 20]"""

#count(찾을 값) : 찾을 값이 몇 개인지 개수를 세서 알려줌
num=[10,20,30,10,40,10,101,10,10]
num.count(10) #num에서 10은 몇개 있는가?
print(int(num.count(10)))
"""5"""
#sort() : 리스트의 값을 정렬함
num=[10,45,23,13,678,42,45,22] #작은 순서대로 정렬해줌
num.sort()
print(num)
"""[10, 13, 22, 23, 42, 45, 45, 678]"""

num=["apple","banana","orange","mango"]
print(num.sort())
#sort(reverse=True) : 내림차순으로 정렬
num=[20,40,10,30,14]
num.sort(reverse=True)
print(num)
"""[40, 30, 20, 14, 10]"""
#reverse() : 그냥 위치를 반대로 바꿔주는거.. 뒤집뒤집.
num=[20,40,10,30,14]
num.reverse()
print(num)
"""[14, 30, 10, 40, 20]"""
#copy() : 복사
num=[20,40,10,30,14]
num2=num.copy()
print(num2) #num2에게 num 의 복사본이 대입됨
"""num=[20,40,10,30,14]"""
#2차원 list
num3=[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]]
for i in range(0,3): #행
    for k in range(0,4): # 열
        print(" ","%3d"%num3[i][k],end=" ")
    print(" ")
    """
    1     2     3     4  
    5     6     7     8  
    9    10    11    12
    """
#4행 5열의 2차원 리스트를 만들고 0부터 3의 배수를 입력하고 출력하도록 하라 => ★어려움!
num=[]
num2=[]
value=0 # => 0부터 시작하니까 value에 0을 넣어준것
for i in range(0,4):
    for k in range(0,5):
        num.append(value)
        value+=3
    num2.append(num)
    num=[]
for i in range(0,4): #0,1,2,3 이렇게 총 4행임 range(시작수,마지막수-1)
    for k in range(0,5):
        print(" ","%3d"%num2[i][k],end=" ")
    print(" ")
"""
0     3     6     9    12  
15    18    21    24    27  
30    33    36    39    42  
45    48    51    54    57
"""
#리스트함축 . 프린트07 17페이지★어려움! 꼭 복습하기
list=[]
for i in range(0,11):
    list.append(i*i)
    print("","%2d"%i,end="")
"""

0  1  2  3  4  5  6  7  8  9 10
"""
#조건연산자
#cost=0 if price>=2000 else 3000 =>price가 2000이 넘으면 cost에 0을 넣고 아니라면 3000을 넣어라
    

#0부터 99까지의 정수 중에서 2의 배수이고 동시에 3의 배수인 수들을 모아 리스트 함축을 사용하여 리스트로 만들어보라
num=[x for x in range(0,100) if x%2==0 and x%3==0]
print(num)
"""
[0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]
"""

#심사위원점수구하기 07-22페이지 밑은 내가 한거
"""
print("홍길동 선수 경기 끝났습니다~~")
a=int(input("평가 점수 ==>"))
b=int(input("평가 점수 ==>"))
c=int(input("평가 점수 ==>"))
d=int(input("평가 점수 ==>"))
e=int(input("평가 점수 ==>"))
f=(a+b+c+d+e)/5
print("심사위원 평균 점수 :","%.1f"%f)
"""
#정답;;
"""
print("홍길동 선수 경기 끝났습니다~~")
score=[]
for i in range(0,5):
    jumsu=int(input("평가 점수 ==>"))
    score.append(jumsu)
hap=0
for i in range(0,):
    hap+=score[i]
average=hap/5
print("심사위원 평균 점수 :",avg)
"""
#두개의 컴퓨터끼리 가위바위보하기
import random
toss=[]
for i in range(0,10000):
    a=random.choice(["가위","바위","보"])
    b=random.choice(["가위","바위","보"])
    if a=="가위":
        if b=="가위":
            toss.append("비김")
        elif b=="바위":
            toss.append("B")
        elif b=="보":
            toss.append("A")
    elif a=="바위":
        if b=="가위":
            toss.append("A")
        elif b=="바위":
            toss.append("비김")
        elif b=="보":
            toss.append("B")
    elif a=="보":
        if b=="가위":
            toss.append("B")
        elif b=="바위":
            toss.append("A")
        elif b=="보":
            toss.append("비김")
Awin=toss.count("A")
Bwin=toss.count("B")
nowin=toss.count("비김")

print("A 컴퓨터의 승리횟수는?: ",Awin)
print("B 컴퓨터의 승리횟수는?: ",Bwin)
print("비긴 횟수는?: ",nowin)
"""
A 컴퓨터의 승리횟수는?:  3347
B 컴퓨터의 승리횟수는?:  3420
비긴 횟수는?:  3233
"""
