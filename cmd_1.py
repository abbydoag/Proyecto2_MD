

import math
import random


def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a
def generar_coprimo(n):
    while True:
        # Genera un número aleatorio entre 1 y n-1 (ambos inclusive)
        m = random.randint(1, n-1)
        # Comprueba si m es coprimo con n
        if math.gcd(n, m) == 1:
            return m  # Retorna m, que siempre será menor que n

def maximo_comun_divisor_recursivo(a, b):
    #Lo mismo que el primero pero simplemente con recursivo
    if b == 0:
        return a
    return maximo_comun_divisor_recursivo(b, a % b)

def inverso_multiplicativo(m, n):
    # Implementa el Algoritmo Extendido de Euclides
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = egcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x, _ = egcd(m, n)
    
    # Verifica si el inverso existe
    if gcd != 1:
        return None  # No existe inverso multiplicativo si gcd(m, n) != 1
    else:
        # Asegúrate de que el resultado esté en el rango [0, n-1]
        return x % n
