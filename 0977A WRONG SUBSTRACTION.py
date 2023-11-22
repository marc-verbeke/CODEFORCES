n, k = map(int, input().split())
for k in range(0,k,1):
    x = str(n)
    if x[-1] != "0":
        n -= 1
    else:
        n = int(n/10)
print(n)