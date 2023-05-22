"""
읽기용 : 변수명=open("파일명","r")
쓰기용: 변수명=open("파일명","w")
r=읽기ver.
w=쓰기
r+ 읽기/쓰기 겸용

*파일을 열때: 변수명=open("파일경로/파일이름","r")
*파일을 닫을때 : 변수명.close();
파일의 내용을 한 행씩  읽을때 : readline()
"""

#myData1.txt
"""
난생처음 파이썬을 공부합니다.
코딩이 재미있어 졋어요.
이젠 코딩 전문가가 된 것 같아요^^
"""
infile=open(r"C:\Users\Sungshin\Desktop\python(월)\5.22/myData1.txt","r",encoding="UTF-8")
#맨앞에 r 쓰는 이유  / 이 아니라 ↖이모양의 슬래쉬를 써야됨 근데 귀찮아서 r씀 , 아니면 // 이렇게 두개 써도됨
#인코딩 쓰는 이유= 한글이라 깨질까봐 방지하기 위해
instr=infile.readline()
print(instr)
"""난생처음 파이썬을 공부합니다."""
instr=infile.readline()
print(instr)
"""코딩이 재미있어 졋어요."""
instr=infile.readline()
print(instr)
"""이젠 코딩 전문가가 된 것 같아요^^"""
infile.close()
print("\n")

infile=open(r"C:\Users\Sungshin\Desktop\python(월)\5.22/myData1.txt","r",encoding="UTF-8")
count=0
while True:
    instr=infile.readline()
    if instr=="":
        break
    count+=1
    print(count,instr,end=" ")
print("\n")
"""
1 난생처음 파이썬을 공부합니다.
 2 코딩이 재미있어 졋어요.
 3 이젠 코딩 전문가가 된 것 같아요^^
 """
#상대경로 : 현재 저장되어있는 파일의 현 위치 ! 힘들게 안찾아도됨 => "./파일이름"
# ex. ("./myData1.txt","r")

#readlines => 파일전체를 읽어옴
infile=open(r"C:\Users\Sungshin\Desktop\python(월)\5.22/myData1.txt","r",encoding="UTF-8")
inlist=infile.readlines()
for instr in inlist:
    print(instr,end=" ")
infile.close()
"""
난생처음 파이썬을 공부합니다.
 코딩이 재미있어 졋어요.
 이젠 코딩 전문가가 된 것 같아요^^
 """

infile=open("./win.ini.txt","r")
inlist=infile.readlines()
for instr in inlist:
    print(instr,end=" ")
infile.close()
