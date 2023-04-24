"""
print(" ##택배를 보내기 위한 정보를 입력하시오.##")
a=input("받는 사람: ")
b=input("주소: ")
c=input("무게(g): ")
print("받는사람==>",a)
print("주소==>",b)

print("배송=>",c*5)

a=int(input("숫자1 ==> "))
b=int(input("숫자2 ==> "))
print(a,"+",b,"=",a+b)
print(a,"-",b,"=",a-b)
print(a,"*",b,"=",a*b)
print(a,"/",b,"=",a/b)
    
    

a=int(input("닭의 수: "))
b=int(input("돼지의 수: "))
c=int(input("소의 수: "))
print("전체 다리의 수 :",a*2+b*4+c*4)

a=int(input("상품의 가격: "))
b=int(input("상품의 개수: "))
c=int(input("부가세: "))
d=int(input("배송료: "))
e=a*b+d+(a*b*0.1)
print("전체가격:","%5.0f"%e)

a=10
b=20
c=10
print("바꾸기 전 : a =",a,"/ b =",b)
a=b
b=c
print("바꾸기 후 : a =",a,"/ b =",b)


a=int(input("교환할 돈은 얼마?"))
b=a//500
print("500원짜리==>",b,"개")
c=a%500//100
print("100원짜리==>",c,"개")
d=a%500%100//50
print("50원짜리==>",d,"개")
e=a%500%100%50//10
print("10원짜리==>",e,"개")
print("바꾸지 못한 잔돈==>",a%500%100%50%10)

편의점 매출 계산하기 =어려웟음
total=0
total-=900*10
total+=1800*2
total-=3500*5
total+=4000*4
total+=1500
total+=2000*4
total+=1800*5
print("오늘 매출액은 ",total,"입니다")

#기말평균 학점구하기
python=3
mobile=2
excel=1
B=3.5
A0=4.0
A=4.5
f=(python*B + mobile*A0+excel*A)/6
print("평균학점 :","%5.2f"%f)

a=52
b=3
print("과자의 개수: ",a)

print("한 사람당 나누어주는 과자의개수 :",b)
print("최대",a//b,"명에게 나누어줄 수 있습니다.")
print("남는 과자는 ",a%b,"입니다.")



a=int(input("삼각형 첫 번째 변의 길이 : "))
b=int(input("삼각형 두 번째 변의 길이 : "))
c=a+b-1
print(c)

a=int(input("시간을 입력하세요 : "))
b=int(input("분을 입력하세요 : "))
print(a,"시간",b,"분은",a*60*60+b*60,"초입니다.")

a=int(input("x의 값을 입력하세요 : "))
b=int(input("y의 값을 입력하세요 : "))
print("(",a,"+",b,")","^","2","=",(a+b)*(a+b))

#이거 어려움 4장 숙
a=int(input("정수 => "))
b=a//1000
c=a%1000//100
d=a%1000%100//10
e=a%1000%100%10
print(b+c+d+e)

#짝수인지 알아보는 프로그램
num=int(input("숫자를 입력하시오:"))
if num%2==0:
    print("작수")
else:
    print("홀수")
"""
"""
90>=A
80>=B
70>=c
60>=D
else F

score=int(input("점수를입력하시오: "))
if score>=90:
    print("a")
elif score>=80:
    print("b")
elif score>=70:
    print("c")
elif score>=60:
    print("d")
else:
    print("f")

score=int(input("나이를입력하시오: "))
if score>=20:
    print("ㄱㅊ")
else:
    print("ㄲㅈ")

#가위바위보게임 > 이거 다시 풀어보기
import random
score=input("나의 가위/바위/보는?: ")
comscore=random.choice(["가위","바위","보"])
print("컴퓨터의 가위바위보는?",comscore)
#random.randint(1,34)는 1부터 34까지 숫자 랜덤추출
#random.choice(["순무1","순무2","순무3"]) 이거는 여기서 랜덤 1개 뽑아줌
if score=="가위":
    if comscore=="가위":
        print("비겼습니다")
    elif comscore=="바위":
        print("이겼습니다")
    elif comscore=="보":
        print("졌습니다")
elif score=="바위":
    if comscore=="가위":
        print("이겼습니다")
    elif comscore=="바위":
        print("비겼습니다")
    elif comscore=="보":
        print("졌습니다")
elif score=="보":
    if comscore=="가위":
        print("졌습니다")


    elif comscore=="바위":
        print("이겼습니다")
    elif comscore=="보":
        print("비겼습니다")
else:
    print("값을 잘못 냈습니다")

#5장조건문
a=int(input("정수를 입력하시오 : "))
b=int(input("정수를 입력하시오 : "))
if a%b==0:
    print("약수입니다")
else:
    print("약수가 아님")

a=int(input("정수를 입력하시오 : "))
if a>0:
    print("양수")
elif a==0:
    print("0")
else:
    print("음수")
    
a=input("문자를 입력하시오 : ")
if a=="r"or a=="R":
    print("네모")
elif a=="t" or a=="T":
    print("세모")
elif a=="c" or a=="C":
    print("원")
else:
    print("unknown")

a=int(input("정수를 입력하시오 : "))
b=int(input("정수를 입력하시오 : "))
c=int(input("정수를 입력하시오 : "))
if a<b:
    if a>c:
        print("제일 작은 정수는",c)
    else:
        print("제일 작은 정수는",a)
elif a>b and b>c:
        print("제일 작은 정수는",c)
else:
    print("제일 작은 정수는 ",a)
    

a=int(input("키를 입력하시오 : "))
b=int(input("나이를 입력하시오 : "))
if a>=140 and b>=10:
    print("ㅇㅋ")
else:
    print("ㄲㅈ")

a=int(input("체중 입력하시오 : "))
b=int(input("키를 입력하시오 : "))
c=(b-100)*0.9
e=a-c
if e<=-10:
    print("저체중")
elif e>=10:
    print("과체중")
else:
    print("표준")
    
    

#for문
for i in range(1,11,1):
    print(i)

sum=0
for i in range(1,11,1):
    sum+=i
print(sum)

name=[1,2,3,4]
for i in name:
    print(i)

num=[1,2,5,16,35]
for i in num:
    if i==2:
        print("찾")
        break
    else:
        print("못찾")
        
#학생줄세우기
i=0
fact=1
for i in range(1,6,1):
    fact*=i
print(fact)

i=0
sum=0
for i in range(1,11,1):
    sum+=i
print(sum)


i=0
sum=0
for i in range(100,301,1):
    if i%5==0:
        sum+=i
print(sum)

i=0
k=0
for i in range(2,10,1):
    for k in range(1,10,1):
        if (i!=5 and k!=5):
            print(i,"x",k,"=",i*k)
        else:
            print(end=" ")
        

i=0
sum=0
while i<10:
    i+=1

    sum+=i
    print(sum)

#100에서 300까지의 5의 배수의 합
i=100
sum=0
while i<=300:
    if i%5==0:
        sum+=i
    i+=1
print(sum)

i=100
sum=0
while i<=300:
    if i%5==0:
        sum+=i
    i+=1
print(sum)

for i in range(2,51,1):
    if i%2==0:
        print(i,end=" ")

list=[11,22,23,99,81,93,35]
sum=0
for i in list:
    sum+=i

print(sum)

for i in range(1,6,1):
    for k in range(1,i+1):
        print(k,end=" ")
    print()

    
for i in range(1,6,1):
    for k in range(1,i+1):
        print(k,end=" ")
    print()
    

i=1.609
print("마일"," ","킬로미터")
for a in range(1,11,1):
    print(a,"%10.3f"%(a*i))
    
i=100
while i<=300:
    if i%5==0:
        i+=1
        
        
print(sum)

sum=0
num1=0
num2=0
while True:
    num1=int(input("숫자1==>"))
    if num1==0:
        break
    num2=int(input("숫자2==>"))
    sum=num1+num2
    print(num1,"+",num2,"=",num1+num2)
print("0을 입력해서 계산을 종료합니다.")

num1,num2=0,0
sum=0
while True:
    num1=int(input("숫자1==>"))
    if(num1==0):
        print("0을 입력해서 종료")
        break
    num2=int(input("숫자2==>"))
    print(num1+num2)
    
sum=0
i=1
while True:
    if i>10:
        break
    sum+=i
    i+=1
    print("i=",i,",","sum=",sum)

i,sum=0,0
for i in range(1,101,1):
    if i%4==0:
        continue
    
    sum+=i
print(sum)

import random
count=0
a,b,c=0,0,0
while True:
    count+=1
    a=random.randint(1,6)
    b=random.randint(1,6)
    c=random.randint(1,6)
    if(a==c)and(c==b):
        break
print(a)
print(count)

import random
count=0
a,b,c=0,0,0
while True:
    count+=1
    a=random.randint(1,6)
    b=random.randint(1,6)
    c=random.randint(1,6)
    if(a==b) and (a==c):
        break
print("숫자는",a)
print("횟수는",count)

import random
user,com=0,0
for i in range(1,11,1):
    com=random.randint(1,5)
    print("게임",i,"회 :",end="")
    user=int(input("컴퓨터가 생각한 숫자는:"))
    if com==user:
        print("맞혔네요. 추카합니다")

        break
    
    else:

        print("까비")
        continue

import random
count=0
a,b,c=0,0,0
while True:
    count+=1
    a=random.randint(1,6)
    b=random.randint(1,6)
    c=random.randint(1,6)
    if (a==c and a==b):
        print("3개 주사위는 모두",a)
        break
print("같은 숫자가 나오기까지",count)
    

i=1
for i in range(1,6,1):
    for k in range(1,i+1,1):
        print(k,end=" ")
    print()
"""
import random
user,com=0,0
for i in range(1,11,1):
    
    com=random.randint(1,5)
    print("게임",i,"회",end="")
    user=int(input("내가 생각한 숫자는"))
    if user==com:
        print("ㅊㅋ")
        break
    else:
        print("까비")
        continue
