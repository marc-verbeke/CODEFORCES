a = input().lower()
b = input().lower()
lijst = []
lijst.append(a)
lijst.append(b)
if max(lijst) > a:
    print(-1)
if max(lijst) > b:
    print(1)
if a == b:
    print(0)
