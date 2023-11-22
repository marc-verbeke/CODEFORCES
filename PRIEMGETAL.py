import math

def check_priemgetal(getal):
    ctrl = 1
    for x in range(2, math.floor(math.sqrt(getal)) + 1, 1):
        if getal % x == 0:
            return False
    return True

def priem(aant):
    p = 2
    for x in range(0, aant, 1):
        if check_priemgetal(p):
            yield(p)
        p += 1

xx = priem(20)
for i in xx:
    print(i)
