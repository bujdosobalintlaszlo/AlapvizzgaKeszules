szamok=input().split(' ')
szam1=int(szamok[0])
szam2=int(szamok[1])
if(szam1==szam2):
    print("egyenlő")
elif(szam1%szam2==0):
    print(f"{szam2} {szam1} osztója")
elif(szam2%szam1==0):
    print(f"{szam1} {szam2} osztója")
else:
    print("relatív prímek")

