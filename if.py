"""
num=int(input())
if num<100:
 print("100보다 작음.")
else:
    print("100보다 큼")

----------------------------------------
num=200
if num>100:
    print("100보다",end="")
    print("큽니다.")
    print("프로그램 끝")
-------------------------------------------

a=200
if a<100:
    print("100보다 작군요.")
    print("거짓임으로 이 문장은 안나옴 ㅋㅋ")

print("end")
#들여쓰기가 중요함 print("end")는 if에 속하지 않기 때문에 들여쓰기 안되도록 조심
-------------------------------------------

city=input()
if city:
    print("너의 도시는: ",city)
else:
    print("입력하삼")
    
-------------------------------------------
score=int(input())
if score>=90:
    print("A")
elif score>=80:
    print("B")

else:
    print("loser")
-------------------------------------------
#3의 배수인지 확인하는문제
num=int(input("숫자를 입력하시오: "))
if num%3==0 and num>=3:
    print("이 숫자는 3의 배수임")
else:
    print("이 숫자는 3의 배수가 아님")
-------------------------------------------

#100<num<1000 이면 pass 100<num, num>1000 이면 fail, num<100이면 loser
num=int(input("숫자를 입력하시오: "))
if num>100:
    if num<1000:
       print("pass")
    else:
        print("fail")
else:
    print("loser")
-------------------------------------------
elif 안쓰고 if로만 중첩문 만드는법 -> 들여쓰기개어려움
score=int(input("점수를 입력하시오: "))
if score>=90:
   print("A학점입니다")
else:
   if score>=80:
        print("B학점입니다")
   else:
       if score>=70:
             print("C학점입니다")
       else:
            if score>=60:
               print("D학점입니다")
            else:
               print("F학점입니다")
-------------------------------------------------------
#elif로 편하게 중첩문 만드는법 -> 쉬움! 이건 들여쓰기 안해도됨
score=int(input("점수를 입력하시오: "))
if score>=90:
   print("A학점입니다")
elif score>=80:
    print("B학점입니다.")
elif score>=70:
    print("C학점입니다.")
elif score>=60:
    print("D학점입니다.")
else:
    print("F학점입니다.")
-----------------------------------------------------------

#삼항연산자
res="합격" if a>=60 else="불합격"
-----------------------------------------------------------
"""


"""
1.수강학점 , 토익점수 입력받기
2.수강학점이 140이상이고 토익점수가 800 이상이면 "졸업"임
3. 두가지 조건을 다 만족해야만 졸업 이고 그렇지 않은 경우에는 "수료" 임

h=int(input("수강학점을 입력하시오: "))
t=int(input("토익점수를  입력하시오: "))

if h>=140:
    if t>=800:
        print("졸업 ㅊㅊ")
else:
    print("수료")
    
#논리연산자로 바꾼거
h=int(input("수강학점을 입력하시오: "))
t=int(input("토익점수를  입력하시오: "))

if h>=140 and t>=800:
   print("졸업")
else:
    print("수료")
------------------------------------------------
1.나이를 입력받는다
2. 5세 미만이면 "영유아"
3. 5세-7세면 "유치부"
4. 8-13세면 초등학생"
5. 14-16세이면 "중딩"
6.17-19세면 " 고딩"
"""
age=int(input("나이를 입력하시오: "))
if age<5:
    print("영유아")
elif age<8:
    print("유치부")
elif age<14:
    print("초딩")
elif age<17:
    print("중딩")
elif age<20:
    print("고딩")
#end="" -> space랑 enter키를 지워주는 거
