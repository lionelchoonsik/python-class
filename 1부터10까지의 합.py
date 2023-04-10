"""
i=0
sum=0
for i in range(1,11):
    sum=sum+i
print("i의 값 :",i,"=>","합계",sum)
"""
#1000부터 2000사이 홀수의 합
i,hap=0,0
for i in range(1001,2001,2):
    hap+=i
print(hap)

#100~300사이 5의배수의 합
i,hap=0,0
for i in range(100,301,5):
    hap+=i
print(hap)


