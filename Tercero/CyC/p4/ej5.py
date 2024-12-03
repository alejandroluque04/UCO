from ej4 import preparenumcipher

# Funcion que cifra los bloques de la lista con la clave que recibe como parametro
def rsacipher(lista_bloques, n, e):
    bloques_cifrados = []

    # el cifrado es bloque^e mod n
    for elemento in lista_bloques:
        bloques_cifrados.append(str(pow(int(elemento), e, n)))
    
    # print(f"Los bloques cifrados quedan asi: {bloques_cifrados}\n")

    return bloques_cifrados



# Funcion que descifra los bloques de la lista con la clave que recibe como parametro
def rsadecipher(bloques_cifrados, n, d):
    tam_bloque = len(str(n)) - 1

    bloques_descifrados = []
    
    # el descifrado es bloque^d mod n
    for elemento in bloques_cifrados:
        bloques_descifrados.append(str(pow(int(elemento), d, n))) 

    # Comprobamos si el bloque descifrado es menor que el tamaño del bloque, si es asi, añadimos 0s al principio
        while len(bloques_descifrados[-1]) < tam_bloque:
            bloques_descifrados[-1] = "0" + bloques_descifrados[-1]    
    
    print(f"Los bloques descifrados quedan asi: {bloques_descifrados}\n")

    return bloques_descifrados



def main():
    n = 64261
    e = 20367
    d = 21379
    cadena_numeros = "12345678"

    lista_bloques = preparenumcipher(cadena_numeros, n)
    bloques_cifrados = rsacipher(lista_bloques, n, e)
    print(f"Los bloques cifrados quedan asi: {bloques_cifrados}\n")
    bloques_descifrados = rsadecipher(bloques_cifrados, n, d)


if __name__ == "__main__":
    main()