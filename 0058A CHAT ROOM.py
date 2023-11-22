s = input()
woord = "hello"
woord1 =""
teller = 0
for x in range(0,len(s),1):
    letter = woord[teller]
    if s[x] == letter:
        woord1 += s[x]
        teller += 1
        if teller >= len(woord):
            break
if woord == woord1:
    print("YES")
else:
    print("NO")