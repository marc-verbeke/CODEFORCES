import math
n, h = map(int, input().split())
a = list(map(int, input().split()))
w = 0
for x in range(0,n,1):
    w += math.ceil(a[x]/h)
print(w)