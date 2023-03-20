
#1번
chicken=int(input("닭의 수 :"))
pig=int(input("돼지의 수 :"))
cow=int(input("소의 수 :"))

print("전체 다리의 수 : ",chicken*2+pig*4+cow*4)

#2번
r=int(input("삼각형의 밑변 :"))
h=int(input("삼각형의 높이 :"))
print("삼각형의 넓이 : ",(r*h)/2)

#3번
money=int(input("상품의 가격 :"))
count=int(input("상품의 개수 :"))
tax=int(input("부가세 :"))
bae=int(input("배송료 :"))
print("전체 가격 : ")
cash=money*count+(money/tax)*count+bae
print("%5d"%cash)


#4번
a=10
b=20
c=10
print("바꾸기 전 : ","a","=",a,"/","b","=",b)
a=b
b=c
print("바꾸기 후 : ","a","=",a,"/","b","=",b)

