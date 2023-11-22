while True:
    n = int(input())
    if 1 <= n <= 100:
        break
woorden = []
for x in range(0,n,1):
    woord = input()
    woorden.append(woord)
for y in woorden:
    if len(y)<=4:
        print(y)
    else:
        print(y[1]+str(len(y))+y[-1])
