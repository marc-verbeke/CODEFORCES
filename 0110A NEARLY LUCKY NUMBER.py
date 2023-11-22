n = input()
ctrl4 = 0
ctrl7 = 0
ctrlelse = 0
for x in range (0,len(n),1):
    if n[x] == "4":
        ctrl4 += 1
    if n[x] == "7":
        ctrl7 += 1
    if n[x] != "4" and n[x] != "7":
        ctrlelse += 1
if ctrl4 > 0 and ctrl7 > 0 and ctrlelse == 0:
    print("YES")
else:
    print("NO")
