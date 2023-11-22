t = int(input())
for x in range(0,t,1):
    n, m = map(int, input().split(' '))
    kaarten = []
    score = 0
    for y in range(0,n,1):
        kaarten.append(list(map(int, input().split(' '))))
    for a in range(0,n,1):
        for b in range(a+1,n,1):
              score += sum([abs(a - b) for a, b in zip(kaarten[a], kaarten[b])])
    print(score)