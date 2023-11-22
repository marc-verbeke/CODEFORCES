afstanden = []
n, l = map(int, input().split(' '))
locaties = sorted(set(list(map(int, input().split(' ')))))
afstanden.append(locaties[0]-0)
for x in range(0,n-1,1):
    afstanden.append((locaties[x+1]-locaties[x])/2)
afstanden.append(l-locaties[n-1])
print(max(afstanden))