# separamos una cadena de números en bloques de tamaño n-1, completando si es necesario con 30s y/o 0
def preparenumcipher(cadena_numeros, n):
    tam_bloque = len(str(n)) - 1

    # añadimos 30 o 0 al final para que la cadena sea divisible por el tamaño del bloque
    while len(cadena_numeros) % tam_bloque != 0:
        
        if (len(cadena_numeros)+1) % tam_bloque == 0:
            cadena_numeros += "0"
        else:
            cadena_numeros += "30"

    print(f"La cadena de números es: {cadena_numeros}\n")

    # dividimos la cadena en bloques de tamaño n-1
    lista_bloques = []
    for bloque in range(0, len(cadena_numeros), tam_bloque):
        lista_bloques.append(cadena_numeros[bloque:bloque+tam_bloque])

    print(f"La lista de bloques es: {lista_bloques}\n")

    return lista_bloques



# concatenamos los bloques de la lista y devolvemos la cadena
def preparetextdecipher(lista_bloques):
    cadena_numeros = ''
    for elemento in lista_bloques:
        cadena_numeros += elemento

    print(f"La cadena queda asi: {cadena_numeros}\n")

    return cadena_numeros




def main():
    n = int(input("Introduce el numero n: \n"))
    while n >= len(cadena_numeros) / 2:
        n = int(input("Tamaño de bloque no válido. Introduce el numero n: \n"))
    
    # lista_bloques = preparenumcipher("0715110019152500110409001303181511211721042504192021030815081306041308041808000813051518120020080200")
    lista_bloques = preparenumcipher("1234567", n)
    cadena_numeros = preparetextdecipher(lista_bloques)
    print()



if __name__ == "__main__":
    main()
    
    
