#임의의 수 여러개를 인수에 넣으면 그 합을 구해주는 함수 (hap(   ) 안에 있는 숫자를 더해줌)
def hap(*seq):
    print(sum(seq))
hap(1,2,3,4) #여기 안에 있는 숫자를 더함
"""10"""

def today(*menu):
    for m in menu:
        print(m)
today("김밥","샐러드","라면","햄버거")
"""
김밥
샐러드
라면
햄버거
"""
