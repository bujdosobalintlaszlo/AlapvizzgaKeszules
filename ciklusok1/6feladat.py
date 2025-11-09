def gcd(n1, n2):
    smaller = n1 if n1 < n2 else n2
    gcd_value = 1
    for i in range(1, smaller + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd_value = i
    return gcd_value

#eukledeszi
def gcdE(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1
