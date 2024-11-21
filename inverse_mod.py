from math import gcd
from re import I
#gcd = mcd
#multiplicación para calcular phi
def calc_phi_n(p,q):
    return (p-1)*(q-1)

def inverso_mod(e,phi_n):
    #calculos de euclides
    def euclides(a,b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = euclides(b, a % b)
        x = y1
        y = x1 -(a//b)*y1
        return gcd, x,y
    gcd, x, _ = euclides(e, phi_n)
    if gcd !=1:
        return None
    return x % phi_n

