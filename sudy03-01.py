'''
money=int(input("교환할 돈은 얼마? "))
c500=money//500 #//은 몫이라는 기호 %는 나머지 라는 기호
print("\n500원짜리 ==>",c500)
r=money%500
c100=r//100
print("\n100원짜리==>",c100,"개")
f=money%500%100
c50=f//50
print("\n50원짜리==>",c50,"개")
g=money%500%100%50
c10=g//10
print("\n50원짜리==>",c10,"개")
h=money%500%100%50%10
print("\n바꾸지 못한 잔돈==> ",h,"원")
'''
num=20
num+=3 #num=num+3
print(num)
num-=3 #num=num3
print(num)
num*=3
print(num)
num/3
print(num)
num//=3#num=num//3
print(num)
num%=3#num=num%3
print(num)
num**=3
print(num)
