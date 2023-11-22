t = int(input())

nummers=[]
for a in range(0,t,1):
    nummers.append(int(input()))

test = False
for aantal in range(0,t,1):
    ctrl = 0
    x = 1
    for y in range(1,nummers[aantal],1):
        z = nummers[aantal] - y - x
        test = True
        if x == y or x == z or y == z:
            test = False
        if x%3 == 0 or y%3 == 0 or z%3 == 0:
            test = False
        if z <= 0:
            test = False
        if test == True:
            ctrl += 1
            break
    if ctrl >= 1:
        print(f"YES \n{x} {y} {z}")
    if ctrl == 0:
        print("NO")

