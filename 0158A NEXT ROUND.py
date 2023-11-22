n, k = map(int, input().split())
uitslag = list(map(int, input().split()))
aantal = 0
for x in range(0,n,1):
    if uitslag[x] >= uitslag[k-1] and uitslag[x] > 0:
        aantal += 1
print(aantal)