k, n, w = map(int, input().split())
totkost = 0
for x in range(0,w,1):
    totkost += (x+1) * k
if totkost - n <= 0:
    print(0)
else:
    print(abs(totkost-n))