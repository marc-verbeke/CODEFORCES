while True:
    n = int(input())
    if 1 <= n <= 100:
        break

liefde = "I love that "
haat = "I hate that "
liefdeslot = "I love it "
haatslot = "I hate it "

gevoel = ""

for x in range(1,n+1,1):
    if x%2 == 0 and x == n:
        gevoel += liefdeslot
        break
    elif x % 2 == 1 and x == n:
        gevoel += haatslot
        break
    elif x%2 == 0:
        gevoel += liefde
    else:
        gevoel += haat

print(gevoel)
