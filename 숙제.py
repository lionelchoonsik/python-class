a=int(input("과자의 개수 : "))
b=int(input("한 사람당 나누어주는 과자의 개수 : "))
c=a//b
d=a%b
print("\n최대",c,"명에게 나누어줄 수 있습니다.")
print("남는 과자는",d,"개입니다.")
print("\n")
a=int(input("삼각형 첫 번째 변의 길이: "))
b=int(input("삼각형 두 번째 변의 길이: "))
c=(a+b)-1
print("삼각형의 나머지 변의 최대길이: ",c)
print("\n")
a=int(input("시간을 입력하세요: "))
b=int(input("분을 입력하세요: "))
c=(a*60*60)+(b*60)
print(a,"시간",b,"분은",c,"초입니다.")
print("\n")
a=int(input("x의 값을 입력하세요: "))
b=int(input("y의 값을 입력하세요: "))
c=(a+b)*(a+b)
print("(",a,"+",b,")","^","2","=",c)
print("\n")
a=int(input("정수 => "))
b=a//1000 #천자리수
c=a%1000//100
d=a%1000%100//10
e=a%1000%100%10
print("합계 : ",b+c+d+e)

