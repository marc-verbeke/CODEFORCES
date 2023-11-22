n, m, a = map(int, input().split(' '))

lengte=0
breedte=0

if n%a == 0:
    lengte=n/a
else:
    lengte=(n//a)+1

if m%a == 0:
    breedte=m/a
else:
    breedte=(m//a)+1
print(int(lengte*breedte))

