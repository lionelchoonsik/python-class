
# 딕셔너리는 2개의 쌍으로 구성되어있음 EX. {키1:값1 , 키2:값2....}
#딕셔너리는 { } 중괄호사용

a=dict(
    name="i",
    id="2212",
    age="14"
    )

print(a)
#추가 append(x) 딕셔너리이름["키"]="값"
a['address']='seoul'
print(a)
"""
{'name': 'i', 'id': '2212', 'age': '14', 'address': 'seoul'}
"""
b=dict(
    sa="1000",
    name="홍길동",
    buseo="케이팝"
    )
print(b)
"""{'sa': '1000', 'name': '홍길동', 'buseo': '케이팝'}"""
b["buseo"]="한빛아카데미"
b["연락처"]="010893789"
print(b)
"""
{'sa': '1000', 'name': '홍길동','buseo': '한빛아카데미', '연락처': '010893789'}
"""
len(b)
print(len(b)) #4나옴
print(b['sa'])
"""1000"""
print(b['name'])
print(b['buseo']) 
print(b['연락처'])
"""
1000
홍길동
한빛아카데미
010893789
"""
# 딕셔너리이름.keys() :키만 뽑아서 출력
print(b.keys())
"""dict_keys(['sa', 'name', 'buseo', '연락처'])"""
# 딕셔너리이름.values() : 값만 뽑아서 출력
print(b.values())
"""dict_values(['1000', '홍길동', '한빛아카데미', '010893789'])"""
## 딕셔너리이름.items() : 튜플형태로 출력
print(b.items())
"""
dict_items([('sa', '1000'), ('name', '홍길동'), ('buseo', '한빛아카데미'), ('연락처', '010893789')])
"""

# in : 딕셔너리 안에 키가 잇는지 확인 가능 .있으면 true  없으면 false 
print("name" in b)
""" true 임"""

#get > 딕셔너리.get(키): 에러 안뜨게 해주는거 , 없더라도 그냥넘어가게해줌
print(a.get("weight")) #에러안뜨고 none 이라고 뜸

for key in b.keys():
    print(key,b[key])
"""
sa 1000
name 홍길동
buseo 한빛아카데미
연락처 010893789
"""


