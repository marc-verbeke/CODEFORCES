
n = int(input())
e = 0
f = 0
g = 0
for a in range(0, n, 1):
    x, y, z = map(int, input().split())
    e += x
    f += y
    g += z
if e != 0 or f != 0 or g != 0:
    print("NO")
else:
    print("YES")