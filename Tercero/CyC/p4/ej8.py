from ej1 import seleccion_primo
from ej2 import keygeneration
from ej3 import NumberToText
from ej4 import preparetextdecipher
from ej5 import rsadecipher
from ej7 import rsaciphertextsign

# Funcion que descifra un mensaje cifrado y una firma cifrada con autenticacion
def rsadeciphertextsign(c1, c2, n_receptor, d_receptor, n_emisor, e_emisor):
    # desciframos con la clave privada del receptor
    bloques_c1 = rsadecipher(c1, n_receptor, d_receptor)
    print(f"Bloques mensaje: {bloques_c1}")

    # vamos a descifrar el mensaje de c1
    cadena_numeros_c1_sucia = preparetextdecipher(bloques_c1)

    cadena_numeros_c1 = ""

    # Comprobamos que la longitud de la cadena sea par, sino, significa que habiamos añadido un 0 al final
    if len(cadena_numeros_c1_sucia) % 2 != 0 and cadena_numeros_c1_sucia[-1] == "0":
            cadena_numeros_c1_sucia = cadena_numeros_c1_sucia[:-1]
    
    # Comprobamos si existe algun bloque que corresponda a 30, si es asi, lo eliminamos
    for par in range(0, len(cadena_numeros_c1_sucia), 2):
        if cadena_numeros_c1_sucia[par:par+2] != "30":
            cadena_numeros_c1 += cadena_numeros_c1_sucia[par:par+2]

    # Desciframos los bloques
    c1_descifrada = NumberToText(cadena_numeros_c1)
    print(f"Texto descifrado: {c1_descifrada}\n")



    # vamos a descifrar la firma de c2. Comenzamos descifrando con la clave privada del receptor
    bloques_c2 = rsadecipher(c2, n_receptor, d_receptor)
    print(f"Bloques firma: {bloques_c2}\n")

    # concatenamos los bloques de la lista y devolvemos la cadena
    cadena_numeros_c2_sucia = preparetextdecipher(bloques_c2)

    cadena_numeros_c2 = ""

    bloques_c2.clear()
    # completamos los bloques hasta que sean de longitud n_receptor-1 y concatenamos
    for i in range(0, len(cadena_numeros_c2_sucia), len(str(n_emisor))):
        if len(cadena_numeros_c2_sucia[i:i+len(str(n_emisor))]) == len(str(n_emisor)):
             bloques_c2.append(cadena_numeros_c2_sucia[i:i+len(str(n_emisor))])       

    # Desciframos los bloques
    bloques_c2_semidescifrado = rsadecipher(bloques_c2, n_emisor, e_emisor)
    
    # concatenamos los bloques de la lista y devolvemos la cadena
    cadena_numeros_c2_sucia = preparetextdecipher(bloques_c2_semidescifrado)
    cadena_numeros_c2 = ""

    # Comprobamos que la longitud de la cadena sea par, sino, significa que habiamos añadido un 0 al final
    if len(cadena_numeros_c2_sucia) % 2 != 0 and cadena_numeros_c2_sucia[-1] == "0":
            cadena_numeros_c2_sucia = cadena_numeros_c2_sucia[:-1]
    
    # Comprobamos si existe algun bloque que corresponda a 30, si es asi, lo eliminamos
    while cadena_numeros_c2_sucia[-2:] == "30":
        cadena_numeros_c2_sucia = cadena_numeros_c2_sucia[:-2]

    cadena_numeros_c2 = cadena_numeros_c2_sucia

    # Desciframos los bloques
    c2_descifrada = NumberToText(cadena_numeros_c2)
    print(f"Firma descifrada: {c2_descifrada}\n")

    return c1_descifrada, c2_descifrada





def main():
    primo1_emisor = seleccion_primo()
    primo2_emisor = seleccion_primo()

    primo1_receptor = seleccion_primo()
    primo2_receptor = seleccion_primo()

    n_emisor, e_emisor, d_emisor = keygeneration(primo1_emisor, primo2_emisor)
    n_receptor, e_receptor, d_receptor = keygeneration(primo1_receptor, primo2_receptor)

    print(f"Claves generadas para el emisor: ({n_emisor}, {e_emisor}), ({n_emisor}, {d_emisor})")
    print(f"Claves generadas para el receptor: ({n_receptor}, {e_receptor}), ({n_receptor}, {d_receptor})")

    texto = "HOLACOMOESTASSOYELEMISOR"
    firma = "SOYELEMISOR"

    bloques_cifrados_texto, bloques_cifrados_firma = rsaciphertextsign(n_receptor, e_receptor, n_emisor, d_emisor, texto, firma)

    c1_descifrada, c2_descifrada = rsadeciphertextsign(bloques_cifrados_texto, bloques_cifrados_firma, n_receptor, d_receptor, n_emisor, e_emisor)
    print(f"Texto descifrado: {c1_descifrada}")
    print(f"Firma descifrada: {c2_descifrada}")



if __name__ == "__main__":
    main()

