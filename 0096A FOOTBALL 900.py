opstelling = input()
teller = 0
letter=""
for x in range(0,len(opstelling)):
    if letter == opstelling[x]:
        teller += 1
    else:
        letter = opstelling[x]
        teller = 1
    if teller >= 7:
        print("YES")
        break
if teller < 7:
    print("NO")