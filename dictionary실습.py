"""
#편의점물품재고관리 ★개어려움
store={} #초기화해주기
print("*** 물품과 재고량 입력***")
while True:
    a=input("입력 물품==> ")
    if a=="z": #z일때 멈추고 다시 되돌아감
        break
count=int(input("재고량 ==>"))
store[a]=count
#key가 a이고 count 가 value임
print("*** 물품과 재고량 입력***")
while True:
    a=input("찾을 물품==> ")
    if a=="":
        break
#만약 찾을 물품이 ""빈칸이 아니라면

    if a in store:
        print(store[a],"개 남았어요")
    else:
         print("그 물품은 없어요.")
        """
#음식궁합
foods=dict(
    떡볶이="오뎅",
    짜장면="단무지",
    라면="김치",
    피자="피클"
    )

while(True):
    i=input(str(list(foods.keys()))+"중에 좋아하는 음식은?") #list로 변환하는 이유는 dict그대로 출력하면 dict.어쩌구 이렇게나와서 안이쁨
    if i in foods:
        print(i,"궁합음식은",foods.get(i),"입니다.")
    elif i=="끝":
        break
    else:
        print("그런 음식이 없습니다. 확인해보세요")
