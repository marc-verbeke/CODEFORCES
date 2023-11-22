n = int(input())
capaciteit = 0
passagiers = 0
for x in range(0,n,1):
    a, b = map(int, input().split())
    passagiers -= a
    passagiers += b
    if passagiers > capaciteit:
        capaciteit = passagiers
print(capaciteit)