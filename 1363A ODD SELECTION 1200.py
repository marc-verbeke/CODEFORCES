import itertools
import math
t = int(input())
ctrl = 0

for a in range(0, t, 1):
    n, x = map(int, input().split(' '))
    reeks = list(map(int, input().split(' ')))
    combinaties = itertools.combinations(reeks, x)
    for comb in combinaties:
        if sum(comb) % 2 == 1:
            ctrl += 1
            break
    if ctrl > 0:
        print("YES")
    else:
        print("NO")
    ctrl = 0
