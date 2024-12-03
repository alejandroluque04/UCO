from ej1 import seleccion_primo
from ej2 import keygeneration
from ej3 import TexttoNumber, NumberToText
from ej4 import preparenumcipher, preparetextdecipher
from ej5 import rsacipher, rsadecipher

# Función que cifra un mensaje recibido como parametro con RSA
def rsaciphertext(cadena):
    # convertimos la cadena a una cadena de números
    cadena_numeros = TexttoNumber(cadena)


    # Vamos a seleccionar dos números primos para generar las claves RSA
    print("Vamos a escoger dos números primos")
    primo1 = seleccion_primo()
    primo2 = seleccion_primo()
    
    # Comprobamos que los números primos sean distintos
    while primo2 == primo1:
        print("El segundo número primo no puede ser igual al primero. Seleccione otro número primo.")
        primo2 = seleccion_primo()

    # Generamos las claves RSA
    n, e, d = keygeneration(primo1, primo2)

    # Convertimos la cadena de números en bloques
    lista_bloques = preparenumcipher(cadena_numeros, n)

    # Ciframos los bloques
    bloques_cifrados = rsacipher(lista_bloques, n, e)

    return bloques_cifrados, n, d




# Función que descifra un mensaje cifrado con RSA
def rsadeciphertext(lista_bloques, n, d):
    # Desciframos los bloques
    bloques_descifrados = rsadecipher(lista_bloques, n, d)

    # Convertimos los bloques en una cadena de números
    cadena_numeros_sucia = preparetextdecipher(bloques_descifrados)

    cadena_numeros = ""
    # Comprobamos que la longitud de la cadena sea par, sino, significa que habiamos añadido un 0 al final
    if len(cadena_numeros_sucia) % 2 != 0 and cadena_numeros_sucia[-1] == "0":
            cadena_numeros_sucia = cadena_numeros_sucia[:-1]

    # Comprobamos si existe algun bloque que corresponda a 30, si es asi, lo eliminamos
    for par in range(0, len(cadena_numeros_sucia), 2):
        if cadena_numeros_sucia[par:par+2] != "30":
            cadena_numeros += cadena_numeros_sucia[par:par+2]


    # Convertimos la cadena de números en una cadena de texto
    cadena = NumberToText(cadena_numeros)

    return cadena


def main():
    # cadena = "HOLA"
    # bloques_cifrados, n, d, tam_bloque = rsaciphertext(cadena)
    # cadena_descifrada = rsadeciphertext(bloques_cifrados, n, d, tam_bloque)
    # print(f"La cadena descifrada es: {cadena_descifrada}")

    print("\n\n")
    cadena = "JASSOLN"
    bloques_cifrados, n, d = rsaciphertext(cadena)
    cadena_descifrada = rsadeciphertext(bloques_cifrados, n, d)
    print(f"La cadena descifrada es: {cadena_descifrada}")



if __name__ == "__main__":
    main()
