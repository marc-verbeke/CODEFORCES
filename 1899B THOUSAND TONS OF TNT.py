t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    mx = []
    camions = []
    gewichten = []

    for x in range(1,n+1,1):
        if n % x == 0:
            camions.append(x)

    for y in range(0,len(camions),1):
        for z in range(0,n,camions[y]):
            gewichten.append(sum(a[z:z + camions[y]]))
        mx.append(max(gewichten)-min(gewichten))
        gewichten = []
    print(max(mx))




