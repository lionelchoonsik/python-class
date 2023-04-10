"""
#1부터 시작해야함 왜냐면 0은 걍안됨

i=0
fact=1
friends_num=5
for i in range(1,friends_num+1,1):
    fact=fact*i
print("줄 세우는 경우의 수는 : ",fact)

#합계를 구하는건?
i=0
fact=0
friends_num=10
for i in range(0,friends_num+1,1):
    fact=fact+i
print("1부터 10까지의 합계는? : ",fact)
"""
#n각형 = 총 n번 밑에걸 반복한다는뜻

import turtle
t=turtle.Turtle()
t.shape("turtle")
s=int(turtle.textinput("","몇각형을 원하시나요?: "))
for i in range(s):
   t.forward(100)
   t.left(360/s)
