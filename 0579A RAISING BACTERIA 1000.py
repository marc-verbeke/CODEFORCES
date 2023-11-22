x = int(input())
teller = 0
for y in range(2,len(bin(x))):
    teller += int(bin(x)[y])
    print(a[y])
print(teller)