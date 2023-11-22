woord = input().lower()
vervanging = {"a": "", "o": "", "y": "", "e": "", "u":  "", "i":"" }
woordzonderklinkers = woord.translate(str.maketrans(vervanging))
puntjeswoord = ""
for x in range(0,len(woordzonderklinkers),1):
    puntjeswoord += str("."+woordzonderklinkers[x])
print(puntjeswoord)