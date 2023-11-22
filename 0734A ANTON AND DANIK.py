n = int(input())
s = input()
teller = 0
for x in range(0,len(s),1):
    if s[x] == "A":
        teller += 1
if teller > n-teller:
    print("Anton")
if teller < n-teller:
    print("Danik")
if teller == n-teller:
    print("Friendship")

