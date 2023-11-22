t = int(input())
for y in range(1,t+1,1):
    n, k = map(int, input().split(' '))
    print(k + ((k-1) // (n-1)))
