from math import gcd
import random
from ej2 import knapsacksol

# funcion que devuelve los factores primos de un numero, sin importar si son repetidos
def factores_primos(n):
    factores = []
    divisor = 2

    # se divide n por el divisor actual hasta que n sea 1, almacenando los factores
    while n > 1:
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 1
    return factores



# funcion que determina si dos numeros tienen factores comunes
def commonfactor(w, s):
    factores_w = set(factores_primos(w))  # Calcula los factores de w una vez

    for elemento in s:
        factores_elemento = set(factores_primos(elemento))  # Calcula los factores de elemento
        factores_comunes = factores_w & factores_elemento  # Intersección

        if factores_comunes:  # Si no está vacío
            print(f"Los factores comunes entre {w} y {elemento} son: {factores_comunes}")
            return True  # Existe algún factor común
        
    return False  # No se encontraron factores comunes


# genera una pareja de claves publica y privada a traves de una mochila supercreciente
def knapsackpublicandprivate(mochila_supercreciente):
    mochila_trampa = []
    m = int(input("Ingrese un valor para m: (recuerda que debe ser mayor o igual que la suma de todos los valores de la mochila)\n"))

    if m < sum(mochila_supercreciente):
        print("El valor de m debe ser mayor o igual que la suma de los elementos de la mochila")
        exit()


    es_coprimo = False

    # ahora se debe escoger el modo de escoger w, que debe ser coprimo con m
    while not es_coprimo:
        print("Ahora se debe escoger el valor de w, que debe ser coprimo con m")
        opcion=int(input("Escoja una opcion:\n\t1. Ingresar un valor para w\n\t2. Generar un valor aleatorio para w\n"))

        # El valor de w lo ingresa el usuario
        if opcion == 1:
            w = int(input("Ingrese un valor para w: (recuerda que debe ser coprimo con m)\n"))
            if gcd(m, w) != 1:
                print("El valor de w debe ser coprimo con m")
            else:
                es_coprimo = True

        # El valor de w se genera aleatoriamente
        elif opcion == 2:
            opc = input("¿Quieres especificar un rango para w? (s/n)\n")
            if opc == "s":
                w_min = int(input("Ingrese el valor mínimo para w:\n"))
                w_max = int(input("Ingrese el valor máximo para w:\n"))

                while w_min > w_max:
                    print("El valor mínimo debe ser menor que el valor máximo")
                    w_min = int(input("Ingrese el valor mínimo para w:\n"))
                    w_max = int(input("Ingrese el valor máximo para w:\n"))

                w = random.randint(w_min, w_max)

                if gcd(m, w) != 1:
                    while not es_coprimo:
                        w = random.randint(w_min, w_max)
                        if gcd(m, w) == 1:
                            es_coprimo = True

                else:
                    es_coprimo = True

            # no se especifica rango
            else:
                w = random.randint(2, m)

                if gcd(m, w) != 1:
                    while not es_coprimo:
                        w = random.randint(2, m)
                        if gcd(m, w) == 1:
                            es_coprimo = True
                
                else:
                    es_coprimo = True

    # Tenemos m y w que son coprimos, comprobamos que w no tenga primos comunes con los elementos de la mochila
    if commonfactor(w, mochila_supercreciente):
        print("El valor de w no debe tener factores comunes con los elementos de la mochila")
        exit()

    # Ahora se deben calcular los valores de la mochila trampa
    mochila_trampa = [(w*a) % m for a in mochila_supercreciente]

    print(f"La mochila trampa es: {mochila_trampa}")
    return w, m, mochila_trampa



# Funcion que halla el inverso modular de un numero p respecto a m
def modinv(p, m):
    if gcd(p, m) != 1:
        return None  # Si no existe el inverso, retorna None
    
    # Algoritmo extendido de Euclides para encontrar el inverso
    inverso, inverso_candidato = 0, 1   
    dividendo, divisor = m, p   
    
    while divisor != 0: 
        cociente = dividendo // divisor 
        inverso, inverso_candidato = inverso_candidato, inverso - cociente * inverso_candidato  # actualizamos los valores de inverso y inverso_candidato
        dividendo, divisor = divisor, dividendo - cociente * divisor    # actualizamos los valores de dividendo y divisor
    
    # Asegurarse de que el inverso esté en el rango [0, n-1]
    if inverso < 0:
        inverso = inverso + m
    
    return inverso



# funcion que descifra un mensaje cifrado con una mochila supercreciente
def knapsackdeciphermh(mochila_supercreciente, m, w, criptograma):
    # Calcular el inverso modular de w respecto a m
    w_inv = modinv(w, m)
    
    mensaje_descifrado = []

    # Descifrar cada valor del criptograma
    for valor in criptograma:
        valor_descifrado = (valor * w_inv) % m  # Calcular el valor descifrado
        solucion = knapsacksol(valor_descifrado, mochila_supercreciente)    
        bloque_bits = [1 if item in solucion else 0 for item in mochila_supercreciente] # Convertir la solución en una lista de bits
        mensaje_descifrado.extend(bloque_bits)
    
    # Convertir la lista de bits en texto
    texto = ''
    for i in range(0, len(mensaje_descifrado), 8):
        byte = mensaje_descifrado[i:i+8]    # Toma los bits en grupos de 8

        # nos aseguramos de que el byte tenga 8 bits, sino se rellena con ceros
        if len(byte) < 8:
            byte.extend([0] * (8 - len(byte)))

        char = chr(int(''.join(map(str, byte)), 2)) # Convierte el byte en un caracter
        texto += char
    
    return texto    


