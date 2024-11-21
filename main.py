from cmd_1 import generar_coprimo, inverso_multiplicativo, maximo_comun_divisor, maximo_comun_divisor_recursivo
from inverse_mod import calc_phi_n
from range_prim import criba


def mostrar_menu():
    print("Menú:")
    print("1. Iniciar")
    print("2. Terminar")

def iniciar():
    str = 0
    
    while str == 0:
        print("1. Encriptar número")
        print("2. Desencriptar número")
        str = input("------> :")
        if str == "1":
            a = 0
            b = 0 
            #Ingresa el número entre los que se darán los números
            print("ingrese el rango de números para los primos (tienen que ser números positivos mayores iguales que 2)")
            a = int(input("a ----> :"))
            b = int(input("b ----> :"))
            a1 = criba(a,b)
            print(a1)
            b2 = criba(a,b)
            print(b2)
            n = a1 * b2
            phi = calc_phi_n(a1,b2)
            e = generar_coprimo(phi)
            print(e)
            d = inverso_multiplicativo(e,phi)
            print(d)
            m = int(input("m ----> número que quiere codificar: "))
            #se hace el calculo para que se de el mensaje códificado
            c =  m**e % n
            print(c)
            print("Tu número de entrada pública es" , e, "Tú número privado es", d, "tú clave para modulo es ", n, "el resultado de la códificación es" , c)
            return
        if str == "2":
            a = 0
            b = 0 
            a = int(input("ingrese llave privada: "))
            b = int(input("ingrese el número N: "))
            c = int(input("ingrese el número codificado: "))
            #se calcula el resultado 
            z = c**a % b
            print("El número original es", z)
            return
        else: 
            print("No valido")
            str = 0

def terminar():
    print("Has elegido la opción 'Terminar'. ¡Adiós!")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1 o 2): ")

    if opcion == '1':
        iniciar()
    elif opcion == '2':
        terminar()
        break  # Sale del bucle y termina el programa
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")
        
#Dados los principios por los que se basa, no se recomienda usar números pequeños bajo nungún prospecto 