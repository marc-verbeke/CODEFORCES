n = int(input())
reeks = list(map(int, input().split(' ')))
test = []
resultaat = []
for x in range(1,n-1,1):
    test = reeks[:]
    print(f"x= {x}")
    for y in range(n-1,x,-1):
        print(f"y= {y}")
        for z in range(x,y+1,1):
            print(f"z= {z}")
            if test[z] == 0:
                test[z] = 9
            if test[z] == 1:
                test[z] = 0
            print(test)
            resultaat.append(sum(test))
        test = reeks[:]
        print (test)
print(max(resultaat))