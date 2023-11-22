n = int(input())

lijst = [4, 7, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
ctrl = 0
for x in lijst:
    if n%x == 0:
        ctrl +=1
if ctrl >= 1:
    print("YES")
else:
    print("NO")