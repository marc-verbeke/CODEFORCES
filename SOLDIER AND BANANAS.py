k = int(input())
n = int(input())
w = int(input())

totaal=0
for x in range(1,w+1,1):
    totaal += x*k
print (totaal-n)