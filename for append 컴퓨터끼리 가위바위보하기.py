import random
toss=[]
for i in range(1000):
    a=random.choice(["가위","바위","보"])
    b=random.choice(["가위","바위","보"])
    
    if a=="가위":
        if b=="가위":
            toss.append("없음")
        elif b=="바위":
            toss.append("B")
        elif b=="보":
            toss.append("A")
    elif a=="바위":
        if b=="가위":
            toss.append("A")
        elif b=="바위":
            toss.append("없음")
        elif b=="보":
            toss.append("B")
    elif a=="보":
        if b=="가위":
            toss.append("B")
        elif b=="바위":
            toss.append("A")
        elif b=="보":
            toss.append("없음")
awin=toss.count("A")
bwin=toss.count("B")
nowin=toss.count("없음")
print(awin)
print(bwin)
print(nowin)
