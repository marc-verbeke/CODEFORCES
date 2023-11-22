def sommatie(getal):
    som = 0
    for x in range(0, len(getal), 1):
        som += int(getal[int(x)])
    return som

t = int(input())

for x in range(0, t, 1):
    n, k = (input().split(' '))
    som = sommatie(n)
    for y in range(int(n),10**10,1):
        if sommatie(str(y)) % int(k) == 0:
            print(y)
            break