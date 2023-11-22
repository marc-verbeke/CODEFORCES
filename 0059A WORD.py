woord = input()
aantlet = len(woord)
teller = 0
for x in range(0,aantlet,1):
    if woord[x].isupper():
        teller = teller +1
if teller>aantlet/2:
   print(woord.upper())
else:
   print(woord.lower())
