
#내부함수는 외부에 있는 함수가 호출하는 것
def outfunc(v1,v2):
    def infunc(num1,num2):
        return num1+num2
    return infunc(v1,v2)
print(outfunc(10,20))
"""30"""
#바로 print(infunc(10,20)) 하면 에러뜸, 내부함수를 한번 호출해줘야함

#lambda함수 : 함수를 한 줄로 간단하게 만들어줌
"""
def 함수이름(매개변수):
    return 결과
    <==>
lambda 매개변수:결과
(ex.print((lambda x,y:x+y)(10,20)) 이렇게 옆에 적기만 하면 끝
"""
print((lambda x,y:x+y)(10,20)) 
"""30"""
def hap(num1,num2):
    res=num1+num2
    return res
print(hap(10,20))
#이거랑 밑에 있는거랑 똑같음!!
hap2=lambda num1,num2:num1+num2
print(hap2(20,10))

#매개변수에 기본값을 설정했을때
hap3=lambda num1=50,num2=3:num1+num2
print(hap3())
"""53"""

#map(함수,리스트) :리스트로부터 원소를 하나씩 꺼내서 함수를 적용시킨다음, 그 결과를 새로운 리스트로 생성
a=[1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i]=int(a[i])
print(a)
"""[1, 2, 3, 4]"""
#i가 0이면 0번째 숫자라서 1.2인데 이걸 int 시키면 1, 1번째숫자는 2.5 -> int 시키면 2....
#위에꺼랑 똑같음!
a=[1.2, 2.5, 3.7, 4.6]
a=list(map(int,a))
print(a)
"""[1, 2, 3, 4]"""

#리스트에 모두 10을 더하는 코드
list=[1,2,3,4,5]
def add10(num):
    return num+10
for i in range(len(list)): #i 가 1,2,3,4,5 니까 len(list)면 5번 반복한다는뜻
    list[i]=add10(list[i]) #i가 0일때 list[0]=1임 list[1]=2,....
print(list)
"""[11, 12, 13, 14, 15]"""
