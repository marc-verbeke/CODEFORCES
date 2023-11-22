x = int(input())
resultaat = 0
for y in range(0,x,1):
    z = input()
    if z == "++X" or z == "X++":
        resultaat += 1
    if z == "--X" or z == "X--":
        resultaat -= 1
print(resultaat)







