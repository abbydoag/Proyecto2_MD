
import random


def criba(n,m):
    if n>m:
        print ("No valido")
        return 0
    
    if n<2:
        print("no valido")
        return 0
    not_prime = set()
    primes = []
    for i in range (n, m):
        if i in not_prime:
            continue
        for j in range(i*n, m, i):
            not_prime.add(j)
        primes.append(i)
        a = random.choice(primes)
    return a


