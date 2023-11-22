def select_kleiner(lst, x):
    reeks = [i for i in lst if i <= x]
    return reeks


n, k = map(int, input().split(' '))
reeks1 = list(map(int, input().split(' ')))
reeks2 = []
maks = max(reeks1)
teller = 0
getal = 0
lengte = 0
if k == 1:
    getal = maks
if k != 1:
    for x in range(1, maks, 1):
        reeks2 = select_kleiner(reeks1, x)
        lengte = len(reeks2)
        if len(reeks2) == k:
            getal = x
            teller += 1
            break
    if teller == 0:
        getal = -1
print(getal)
