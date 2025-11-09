szamok=input().split(' ')
osszeg=int(szamok[0]) + int(szamok[1])
if(osszeg%2==0):
    print("paros")
else:
    print("paratlan")