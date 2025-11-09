szam = int(input("Adj meg egy egész számot: "))

faktorialis = ""
oszto = 2

while szam > 1:
    if szam % oszto == 0:          # Ha osztható
        #print(f"{oszto}*")
        faktorialis+=f"{oszto}*"                           #faktorialis.append(oszto) # Hozzáadjuk a listához
        szam = szam // oszto      # Elosztjuk
    else:
        oszto += 1                 # Próbáljuk a következő osztót
print(faktorialis)
