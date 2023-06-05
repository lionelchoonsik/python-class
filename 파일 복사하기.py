# "r" = 읽어온다는 뜻 "w"=적기모드

infile,outfile=None,None
instr=""
infile=open("./myData3.txt","r")
outfile=open("./myNote.txt","w")

inlist=infile.readlines()
for instr in inlist:
    outfile.writelines(instr)

infile.close()
outfile.close()
print("복사완료")
