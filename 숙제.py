
#1번
i=0
for i in range(2,51,2):
    if i%2==0:
        print(i,end=" ")
print("\n")

#2번

hap=0
for i in [11,22,23,99,81,93,35]:
    hap=hap+i
print("정수들의 합은",hap)
print("\n")

#3번
a=int(input("정수를 입력하시오 :"))
print("약수 : ",end="")
for i in range(1,a+1):
    if a%i==0:
        print(i,end=' ')
print("\n") 
#4번
for i in range(1,6):
    for k in range(1,i+1):
        print(k,end=" ")
    print()
print("\n")    
#5번
i=1.609
for a in range(1,11,1):
    print("마일","%10s"%("킬로미터"))
    print("%-7s"%(a),"%10s"%(a*i))
    print()
