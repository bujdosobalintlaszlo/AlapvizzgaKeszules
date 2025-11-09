#beolvasom az adatokat
n1=int(input())
n2=int(input())
#megnezem melyik a kisebb mert addig megy majd a ciklus
kisebb = n1 if n1 < n2 else n2
#lnko
gcd_val = 1
# 1tol megyek egesze kisebb ertek+1 ig, mert [1,kisebb+1[ az intervallum
for i in range(1, kisebb + 1):
    #ha i mindekttot osztja akkor az lnko az lesz
    if n1 % i == 0 and n2 % i == 0:
        gcd_val = i
print(gcd_val)


