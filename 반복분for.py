
for i in range(3):
    print("안뇽")
    print(i)
          
for a in range(5):
    print("soonmu")
    print(a)

print("\n")
"""
range(n) : 0부터 n-1까지의 정수
ex) range(3) : [0,1,2]

range(s,n) :s부터 n-1까지의 정수 범위
ex) range(2,7) :[2,3,4,5,6]

range(s,n,step) :s부터 step 간격으로 n-1까지의 정수 범위
ex) range(1,7,2) :[ 1,3,5 ]

★※여기서 중요한건  range(2,7)=> 2부터 6까지라는 것이다....!!!!!!!!!!!!!!!!

(a,b)면 b-1이 마지막 숫자임 
"""

for i in range(5):
    print(i)
    
for i in range(2,5):
    print(i)

for i in range(2,5,2):
    print(i)
for i in range(1,11):
    print(i)
print("\n")

#역순으로 출력하는법 (역순은 (s,n-1,-1)이래야함 n은 출력하고자 하는 마지막 수)
#원래 일반은 range(s,n+1,1) 이게 정상임 range(0,5,1):0,1,2,3,4 //range(4,-1,-1):4,3,2,1,0
for i in range(10,0,-1): #10에서 1까지 -1간격으
    print(i)
