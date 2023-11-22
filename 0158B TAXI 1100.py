n = int(input())
lijst = list(map(int, input().split(' ')))
aanteen = 0
aanttwee = 0
aantdrie = 0
aantvier = 0
aanttaxi = 0
for x in range(0,n,1):
    if lijst[x] == 1:
        aanteen += 1
    if lijst[x] == 2:
        aanttwee += 1
    if lijst[x] == 3:
        aantdrie += 1
    if lijst[x] == 4:
        aantvier += 1

print(aanteen)
print(aanttwee)
print(aantdrie)
print((aantvier))
print(f"aantal taxi {aanttaxi}")

aanttaxi += aantvier
aantvier = 0

aanttaxi += aantdrie
aanteen -= aantdrie
if aanteen < 0:
    aanteen = 0
aantdrie = 0

aanttaxi += aanttwee//2
aanttwee -= aanttwee//2*2

if aanttwee%2 == 1:
    aanttaxi +=1
    aanttwee -= 1
    aanteen -= 2
    if aanteen < 0:
        aanteen = 0

aanttaxi += aanteen//4
aanteen -= aanteen//4 * 4
if aanteen <= 0:
    aanteen = 0
else:
    aanttaxi += 1
    aanteen = 0

print(aanteen)
print(aanttwee)
print(aantdrie)
print((aantvier))

print(f"aantal taxi {aanttaxi}")