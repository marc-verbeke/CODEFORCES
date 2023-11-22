n = int(input())
fibo = [1, 2]
element = 0
if n > 2:
    for x in range(2,n,1):
        element = fibo[x-1] + fibo[x-2]
        fibo.append(element)
print(fibo[n-1])
