#★★개어려움 집에서 제발 공부 ㄱ


#ord= 문자를 숫자로 바꿔주는 함수 ex. ord("난")  => 45212
#chr = 숫자 -> 문자 바꿔줌 ex. chr(45212) =>"난"

#입력할 문자열 instr / 암호를 저장할 문자열 secure
securefile=None
instr,secure="",""
securefile=open("./myData3.txt","w",encoding="UTF-8") #한글로 쓸거면 인코딩 해주는게 좋음

while True:
    instr=input("스파이에게 전달할 메시지 ==>")
    if instr=="":
        break
    for ch in instr:
        num=ord(ch)
        num+=100
        secure+=chr(num)
securefile.writelines(secure)
securefile.close()
print("암호화 완료")
"""
스파이에게 전달할 메시지 ==>파이썬
스파이에게 전달할 메시지 ==>최고
스파이에게 전달할 메시지 ==>
암호화 완료

메모장=>퍰쟘쏐췀굄
"""

#텍스트 파일 입출력 (9강 48p)

##변수선언부분##
infp,outfp=None,None
instr,outstr="",""
i=0
secu=0

##메인코드부분##
secu2=input("1.암호화 2. 암호해석 중 선택 : ")
infname=input("입력 파일명을 입력하세요 :")
outfname=input("출력 파일명을 입력하세요 :")
if secu2=="1":
     secu=100
elif secu2=="2":
     secu=-100
infp=open(infname,"r",encoding="utf-8")
outfp=open(outfname,"w",encoding="utf-8")

while True:
    instr=infp.readine()
    if not instr:
        break

    outstr=""
    for i in range(0,len(instr)):
        ch=instr[i]
        chnum=ord(ch)
        chnum=chnum+secu
        ch2=chr(chnum)
        outstr=outstr+ch2

    outfp.write(outstr)

outfp.close()
infp.close()
print("변환완료")
