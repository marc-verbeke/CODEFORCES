import math
n, m, a, b = map(int, input().split(' '))
kost = []
kost.append((n//m*b)+(n%m*a))
kost.append(n*a)
kost.append((n//m*b)+(n%m*b))
kost.append(math.ceil(n/m)*b)
print(min(kost))