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

