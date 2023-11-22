n = int(input())
lijst = list(map(int, input().split()))
if sum(lijst)>0:
    print("HARD")
else:
    print("EASY")