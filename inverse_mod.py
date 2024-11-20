from math import gcd
from re import I
#gcd = mcd

def calc_phi_n(p,q):
    """
    n y ϕ(n)
    """
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

#Inputs
p = int(input("Ingrese el valor de p (primo 1): ")) 
q = int(input("Ingrese el valor de p (primo 2): "))
e = int(input("Ingrese el valor de e: ")) 

#N y phi
n = p*q
phi_n = calc_phi_n(p, q)
print(f"n = {n}")
print(f"ϕ({n}) = {phi_n}")

# verificar rango para e
if gcd(e, phi_n) != 1:
    print(f"El valor de e = {e} no es válido ya que no es coprimo con ϕ(n)")
#Inverso modular
else:
    inverso = inverso_mod(e, phi_n)
    if inverso is not None:
        print(f"El inverso modular de '{e} mod {phi_n}' es: {inverso}")
    else:
        print(f"No existe un inverso modular para '{e} mod {phi_n}'")