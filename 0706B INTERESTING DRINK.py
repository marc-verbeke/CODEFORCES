n = int(input())
shops = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    m = int(input())
    teller = sum(1 for shop in shops if shop <= m)
    print(teller)