'''
en megoldasom
def primeFact(n):
    tenyezok = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            tenyezok.append(i)
            n //= i
        i += 1
    if n > 1:
        tenyezok.append(n)
    print("*".join(map(str,tenyezok)))

#fv. meghivasa
primeFact(360)
primeFact(13)

#tesztelesnel hatekonyabb lehet
testCases=[16,4,8,13,360,52,43,892]
for i in testCases:
    primeFact(i)
'''
