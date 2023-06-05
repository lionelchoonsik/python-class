# with open("./파일이름","w")as 구문:


#리스트에 들어있는 문자열을 파일에 쓰기
lines=["안녕하세요\n","파이썬\n","코딩도장입니다.\n"]

with open("./myNote.txt","w",encoding="utf-8")as file:
    file.writelines(lines)
"""
안녕하세요
파이썬
코딩도장입니다.
"""
