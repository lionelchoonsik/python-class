"""
#( ) 안에 있는 정수 중 하나를 랜덤하게 뽑하내는 것 =rand int
import random 선언하고
random.randint(1,45)


#숫자가 아닌경우는? list[] 써주기!
rand.choice["김밥","라볶이","돈가스","짜장면"]
"""

import random
my=input("내가 낸 가위/바위/보 는? : ")
computer=random.choice(["가위","바위","보"])
print("컴퓨터의 가위/바위/보 는?:",computer)

if my=="가위":
    if computer=="가위":
        print("비겼습니다")
    elif computer=="바위":
        print("졌습니다")
    elif computer=="보":
        print("이겼습니다")
elif my=="바위":
    if computer=="가위":
        print("이겼습니다")
    elif computer=="바위":
        print("비겼습니다")
    elif computer=="보":
        print("졌습니다")
elif my=="보":
    if computer=="가위":
        print("졌습니다")
    elif computer=="바위":
        print("이겼습니다")
    elif computer=="보":
        print("비겼습니다")
