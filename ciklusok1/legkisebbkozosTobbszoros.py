szam1 = int(input("Írd be az első számot: "))
szam2 = int(input("Írd be a második számot: "))

# Eldöntjük, melyik a nagyobb
if szam1 > szam2:
    nagyobb = szam1
else:
    nagyobb = szam2

lkkt = nagyobb
#ez azt tudja, hogy a végtelenségig megy. van benne a break, akkor lép ki
#ebből. legrosszabb esetben a ket szam szorzatanal
while True:
    if lkkt % szam1 == 0 and lkkt % szam2 == 0:
        print("A legkisebb közös többszörös:", lkkt)
        break
    #ha nem jo lepunk a nagyobb szammal
    lkkt += nagyobb
