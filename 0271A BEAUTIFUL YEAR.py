while True:
    jaar = input()
    if 1000 <= int(jaar) <= 9000:
        break
cijfers="1234567890"
ctrl = False
for x in range(int(jaar)+1,10000,1):
    for y in cijfers:
        z=str(x).count(y)
        if z == 1 or z == 0:
            ctrl = True
        else:
            ctrl = False
            break
    if ctrl == True:
        print(x)
        break