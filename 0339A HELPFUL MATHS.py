resultaat = ""
lijst = sorted(list(map(int, input().split("+"))))
for x in range(0,len(lijst),1):
    if x == 0:
        resultaat += str(lijst[x])
    else:
        resultaat += "+"+str(lijst[x])
print(resultaat)