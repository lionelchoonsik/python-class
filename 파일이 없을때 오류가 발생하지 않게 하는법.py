"""
import os
inFp=None #값이 존재하지 않는 경우
fName,inList,inStr="",[],""
fName=input("파일명을 입력하세요 :")

if os.path.exists(fName):
    inFp=open(fname,"r")

    inList=inFp.readlines()
    for inStr in inList:
        print(instr,end="")

        inFp.close()

else:
    print("파일이 없습니다")
"""
#내가 입력한 내용을 한 행씩 파일에 쓰기 > 뭔가 중요해보임

outfile=None
outstr=""
outfile=open("./myData3.txt","w")

while True:
    outstr=input("내용 입력==>")
    if outstr !="":
        outfile.writelines(outstr+"\n")
    else:
        break
outfile.close()
print("파일이 저장됨")
