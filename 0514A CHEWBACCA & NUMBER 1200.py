x = input()
y = len(x)
z = int(x)
for a in range(0,y,1):
    if 9-int(x[a]) < int(x[a]):
        z = z - int(x[a])*10**(y-a-1) + ((9 - int(x[a]))*10**(y-a-1))
if x[0]=="9":
    z += 9 *10**(y-1)
print(z)
