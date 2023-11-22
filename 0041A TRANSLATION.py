woord1 = input()
woord2 = input()
droow = ""
for x in range (-1,-1*(len(woord1)+1),-1):
    droow += woord1[x]
if droow == woord2:
    print("YES")
else:
    print("NO")