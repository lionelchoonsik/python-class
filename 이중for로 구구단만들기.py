"""
i,k=0,0
for i in range(2,10,1):
    for k in range(1,10,1):
        print(i,"*",k,"=",i*k)
        print("")
"""
a=int(input("몇단을 출력할까요?: "))
for i in range(1,10):
    c=a*i
    print(a,"*",i,"=",c)
