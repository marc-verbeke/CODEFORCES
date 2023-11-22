n, k = map(int,input().split())
latten = list(map(int, input().split()))
klein = 1.5*(10**6)
som = 0
pos = 0
for x in range(0,n-k+1,1):
    for y in range(0,k,1):
        som += latten[x+y]
    if som < klein:
        klein = som
        pos = x+1
    som = 0
print(pos)