from math import gcd
from random import randint
from ej1 import seleccion_primo

# Función que genera las claves pública y privada a partir de dos números primos
def keygeneration(primo1, primo2):
    # Calculamos n y phi
    n = primo1 * primo2
    phi = (primo1 - 1) * (primo2 - 1)
    print(f"n = {n}, phi = {phi}")

    # vamos a dar un valor a e
    print("Seleccione una opcion. Recuerde que e debe ser coprimo con phi y menor que phi\n\t1. 1. Introducir valor de e\n\t2. Elegir un valor aleatorio de e")
    if phi > 65537:
        print("\t3. e = 65537 (primo de Fermat)")

    opcion = int(input())

    # OPCION 1: Introducir valor de e. Debemos comprobar que e es coprimo con phi y menor que phi
    if opcion == 1:
        e = int(input("Introduzca el valor de e: "))
        while gcd(e, phi) != 1 or e >= phi:
            if gcd(e, phi) != 1:
                print("e no es coprimo con phi. Introduzca el valor de e: \n")
            else:
                print("e debe ser menor que phi. Introduzca el valor de e: \n")
            e = int(input("Valor no valido. Introduzca el valor de e: \n"))

    # OPCION 2: Elegir un valor aleatorio de e. Debemos comprobar que e es coprimo con phi y menor que phi
    elif opcion == 2:
        e = randint(2, phi - 1)
        while gcd(e, phi) != 1 or e >= phi:
            e = randint(2, phi - 1)

    # OPCION 3: e = 65537 (primo de Fermat). Solo si phi es mayor o igual que 65537
    elif opcion == 3 and phi >= 65537:
        e = 65537

    else:
        print("Opción no válida")
        return False, False, False 
        
    # nos aseguramos de que e es coprimo con phi
    if gcd(e, phi) != 1:
        return False, False, False

    d = pow(e, -1, phi)

    # Clave pública: (n, e), clave privada: (n, d)
    print(f"Clave pública: ({n}, {e})")
    print(f"Clave privada: ({n}, {d})\n")
    return n, e, d



def main():
    primo1 = seleccion_primo()
    primo2 = seleccion_primo()

    n, e, d = keygeneration(primo1, primo2)

    if n:
        print("Claves generadas correctamente")
    else:
        print("Error al generar las claves")



if __name__ == "__main__":
    main()



# EJEMPLO DE USO:
# PRIMO1: 359   PRIMO2: 179 N: 64261    E: 20367    D: 21379