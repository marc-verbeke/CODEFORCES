woord = input()
woordC = [woord[0].capitalize()]
for x in range(1, len(woord), 1):
    woordC.append(woord[x])
print("".join(woordC))