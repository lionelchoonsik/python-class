
#1번
a=int(input("정수를 입력하시오 :"))
b=int(input("정수를 입력하시오 :"))

if a%b==0:
    print("약수입니다.")
else:
    print("")
    
print("\n")
#2번
a=int(input("정수를 입력하시오 : "))
if a>0:
    print("양수")
elif a==0:
    print("0")
elif a<0:
    print("음수")
    
print("\n")
#3번
a=input("문자를 입력하시오 : ")
if a=="R" or a=="r":
     print("Rectangle")
elif a=="T" or a=="t":
    print("Triangle")
elif a=="C" or a=="c":
    print("Circle")
else:
    print("Unknown")

print("\n")
#4번
a=int(input("첫 번째 정수를 입력하시오 : "))
b=int(input("두 번째 정수를 입력하시오 : "))
c=int(input("세 번째 정수를 입력하시오 : "))
if a<b:
    if a<c:
        print("제일 작은 정수는",a,"입니다.")
elif b<a and b<c:
    print("제일 작은 정수는",b,"입니다.")
else:
    print("제일 작은 정수는",c,"입니다.")

print("\n")
#5번
a=int(input("키를 입력하시오(cm): "))
b=int(input("나이를 입력하시오(cm): "))
if a>=140 and b>10:
    print("타도 좋습니다.")
else:
    print("죄송합니다.")

print("\n")

#6번
a=int(input("체중을 입력하시오(kg): "))
b=int(input("키를 입력하시오(cm): "))
if a<=(b-100)*0.9-10:
    print("저체중입니다.")
elif a>=(b-100)*0.9+10:
    print("과체중입니다.")
else:
    print("표준체중입니다.")
