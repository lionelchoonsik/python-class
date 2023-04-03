"""파이썬 3학점
모바일 2학점
엑셀 1학점"""

python=3
mobile=2
excel=1

A=4.5
A0=4
B=3.5

average=((python*B)+(mobile*A0)+(excel*A))/python+mobile+excel
print("평균학점:","%7.2f" %average)
#7은 자리수 빼도 상관없음 %.2f 가 소수점 두자리까지 나오게 하는필수
