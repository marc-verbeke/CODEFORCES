n = int(input())
fibi = [1, 2]
for x in range(2, 20, 1):
    fibi.append(fibi[x - 2] + fibi[x - 1])
print(fibi[n - 1])
print(fibi)
