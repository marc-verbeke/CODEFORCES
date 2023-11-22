t = int(input())
for x in range(0,t,1):
    n = int(input())
    if (n-1)%3 == 0 or (n+1)%3 == 0:
        print("First")
    else:
        print("Second")