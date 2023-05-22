my=[1,2,3,4,5]
add10=lambda num:num+10
my=list(map(add10,my))
print(my)
"""[11, 12, 13, 14, 15]"""

#두 리스트의 각 자릿수를 합쳐서 새로운 리스트로 만들기
list1=[1,2,3,4]
list2=[10,20,30,40]
haplist=list(map(lambda n1,n2:n1+n2,list1,list2))
print(haplist)
"""[11, 22, 33, 44]"""

#재귀함수 : 자신이 자신을 호출
def selfcall():
    print("하",end='')
    selfcall()
#selfcall()
"""
하하하하하하하.... x 무한반복;;;
"""
#횟수 count를 주고 반복!
def count(num):
    if num>=1:
         print(num,end=" ")
         count(num-1)
    else:
        return
count(10)
print("\n")
count(5)
"""
10 9 8 7 6 5 4 3 2 1 

5 4 3 2 1
"""
#factorial  값을 구하는 함수
def factorial(num):
    if num<=1:
        return num
    else:
        return num*factorial(num-1)
    
print(factorial(4))
"""5 4 3 2 1 24""""


