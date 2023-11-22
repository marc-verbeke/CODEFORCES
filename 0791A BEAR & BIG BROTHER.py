a, b = map(int, input().split(' '))

jaar = 0

while True:
    jaar=jaar+1
    if (a*3**jaar) > (b*2**jaar):
        print(jaar)
        break