"""
★함수의 형태

#함수정의
define 여서 def

EX)def 함수이름():
           a=10
           b=20
           c=a+b
#변수 선언
#연산 및 처리 구현

def happ(): ->매개변수 없는 ver.
    num1=int(input("정수를입력하시오"))
    num2=int(input("정수를입력하시오"))
    return num1+num2 
print("A님  두 숫자를 입력하시오")
hap=happ()
print("결과 :",hap)

print("b님  두 숫자를 입력하시오")
hap=happ()
print("결과 :",hap)

print("c님  두 숫자를 입력하시오")
hap=happ()
print("결과 :",hap)
----------------------------------------------------------------------

def uchang(v1,v2): #이걸 괄호안에 매개변수가 있는 ver.
    result=0 #일단초기화
    result=v1+v2
    return result
hap=0

hap=uchang(100,100)
print(hap)
"""
#함수를 사용한 계산기 구현 (계산결과를 저장할 변수:res ,연산자:v3 , 두숫자:v1,v2
def mix(v1,v2,v3):
    result=0
    if v3=="+":
        result=v1+v2
    elif v3=="-":
        result=v1-v2
    elif v3=="-":
        result=v1-v2
    elif v3=="*":
        result=v1*v2
    elif v3=="/":
        result=v1/v2
    return result
res=0
var1,var2,var3=0,0,""
var3=input("계산입력(+,-,*,/) : ")
var1=int(input("첫번째 숫자 입력 :"))
var2=int(input("두번째 숫자 입력 :"))
res=mix(var1,var2,var3)
print(var1,var3,var2,"=",res)
