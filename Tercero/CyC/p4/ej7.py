from ej1 import seleccion_primo
from ej2 import keygeneration
from ej3 import TexttoNumber
from ej4 import preparenumcipher, preparetextdecipher
from ej5 import rsacipher

# Funcion que cifra un mensaje_firma y firma de autenticidad con RSA. Ciframos el mensaje con la clave publica del receptor y la
# firma con la clave privada del emisor y la clave publica del receptor
def rsaciphertextsign(n_receptor, e_receptor, n_emisor, d_emisor, texto, firma):
    # Pasamos el texto y la firma a numeros
    cadena_numeros = TexttoNumber(texto)
    firma_numeros = TexttoNumber(firma)

    # Preparamos los bloques para cifrar
    lista_bloques_texto = preparenumcipher(cadena_numeros, n_receptor)
    lista_bloques_firma = preparenumcipher(firma_numeros, n_emisor)

    # ciframos el texto con la clave publica del receptor
    bloques_cifrados_texto = rsacipher(lista_bloques_texto, n_receptor, e_receptor)

    # ciframos la firma con la clave privada del emisor
    bloques_cifrados_firma = rsacipher(lista_bloques_firma, n_emisor, d_emisor)

    firma_numeros = ""

    # Completamos los bloques de la firma hasta que tengan la longitud de n_emisor
    for bloque in bloques_cifrados_firma:
        while len(bloque) < len(str(n_emisor)):
            bloque = "0" + bloque
        firma_numeros += bloque

    # Preparamos los bloques de la firma para cifrar, separando los bloques de la firma en bloques de longitud n_receptor-1
    bloques_cifrados_firma = preparenumcipher(firma_numeros, n_receptor)

    # Ciframos la firma con la clave publica del receptor
    bloques_cifrados_firma = rsacipher(bloques_cifrados_firma, n_receptor, e_receptor)

    return bloques_cifrados_texto, bloques_cifrados_firma



def main():
    primo1_emisor = seleccion_primo()
    primo2_emisor = seleccion_primo()

    primo1_receptor = seleccion_primo()
    primo2_receptor = seleccion_primo()

    n_emisor, e_emisor, d_emisor = keygeneration(primo1_emisor, primo2_emisor)
    n_receptor, e_receptor, d_receptor = keygeneration(primo1_receptor, primo2_receptor)

    print(f"Claves generadas para el emisor: ({n_emisor}, {e_emisor}), ({n_emisor}, {d_emisor})")
    print(f"Claves generadas para el receptor: ({n_receptor}, {e_receptor}), ({n_receptor}, {d_receptor})")

    texto = "HOLACOMOESTAS"
    firma = "SOYELEMISOR"

    bloques_cifrados_texto, bloques_cifrados_firma = rsaciphertextsign(n_receptor, e_receptor, n_emisor, d_emisor, texto, firma)
    print()



if __name__ == "__main__":
    main()