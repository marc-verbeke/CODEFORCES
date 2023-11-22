t = int(input())
karakters = ["1","2","3","4","5","6","7","8","9","0"]
for x in range(0,t,1):
    reeks = input()
    sec = 0
    karakter1 = "1"
    for y in range(0,4,1):
        karakter2 = reeks[y]
        index1 = karakters.index(karakter1)
        index2 = karakters.index(karakter2)
        sec += (1 + abs(index2 - index1))
        karakter1 = karakter2
        if y == 3:
            print(sec)


