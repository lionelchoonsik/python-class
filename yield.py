#yield : 함수를 종결하지 않으면서 값을 계속 반환
def genFunc(num):
    for i in range(0,num):
        yield i
        print("제너레이터 진행중")
for data in genFunc(5): #5 삽입
    print(data)
"""
0
제너레이터 진행중
1
제너레이터 진행중
2
제너레이터 진행중
3
제너레이터 진행중
4
제너레이터 진행중
"""
#제너레이터함수는 yield가 포함된 함수이
