
a={1:10,2:20}
a[3]=30
print(a)

d={1:10,2:20,3:30,4:40,5:50,6:60}
print(" ")

while(True):
    a=int(input("키를 입력하시오 :"))
    if a in d:
        print("키",a,"는 딕셔너리에 있습니다.")
    else:
        print("키가 없습니다.")
        break
print(" ")

myDict=dict(
    옷=100,
    컴퓨터=2000,
    모니터=320
    )
print(sum(myDict.values()))
#sum!!!!!!! 합계구할수있음
