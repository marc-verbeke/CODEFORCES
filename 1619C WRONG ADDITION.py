t = int(input())
z = 0
for x in range(0,t,1):
    b = ""
    a, s = map(str, input().split(' '))
    z = int(len(s) - 1)
    for y in range(len(a)-1, -1, -1):

        if int(s[z])-int(a[y]) >= 0:
            b = str(int(s[z])-int(a[y])) + b
            z -= 1
        elif int(s[z]) - int(a[y]) < 0:
            b = str(int(str(s[z-1])+str(s[z])) - int(a[y])) + b
            z -= 2
    print(b)

