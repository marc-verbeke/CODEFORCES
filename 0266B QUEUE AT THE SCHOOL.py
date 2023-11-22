n, t = map(int, input().split())
s = list(input())
for t in range(0,t,1):
    ctrl = 1
    for x in range (0,n-1,1):
        if ctrl == 1:
            if s[x] == "B" and s[x+1] == "G":
                s[x], s[x+1] = s[x+1], s[x]
                x += 1
                ctrl = 0
        else:
            ctrl = 1
print(''.join(s))