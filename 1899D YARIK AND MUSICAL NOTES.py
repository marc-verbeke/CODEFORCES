import itertools

t = int(input())
combs = []
machten = []

for a in range(0,t,1):
    n = int(input())
    lijst = list(map(int, input().split()))
    combs.extend(itertools.permutations(lijst, 2))
    print((combs))
    for b in range(0,len(combs),1):
        if combs[b][0]<combs[b][1]:
            machten.append(combs[b][0]**combs[b][1])
            macht = set(machten)
    print(sorted(macht))
    print(len(macht))
