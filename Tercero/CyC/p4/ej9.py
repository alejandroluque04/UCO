from ej1 import seleccion_primo
from ej3 import TexttoNumber, NumberToText
from ej4 import preparenumcipher, preparetextdecipher
from math import gcd


# funcion para obtener las claves publicas y la compartida
def obtener_claves(q, g):
    # Seleccion de las claves privadas
    c_priv_emisor = int(input(f"Introduzca el número a. Recuerde que debe estar entre 2 y {q-2}\n"))
    c_priv_receptor = int(input(f"Introduzca el número b. Recuerde que debe estar entre 2 y {q-2}\n"))

    # Calculo de las claves públicas
    clave_publica_emisor = pow(g, c_priv_emisor, q)
    clave_publica_receptor = pow(g, c_priv_receptor, q)

    # Calculo de la clave compartida
    gak = pow(g, c_priv_emisor*c_priv_receptor, q)

    return clave_publica_emisor, clave_publica_receptor, gak


# funcion que cifra los bloques de un mensaje aplicando la formula c = m*g^ak mod q
def cifrar(m_bloques, gak, q):
    c_bloques = []
    for bloque in m_bloques:
        c_bloques.append(str((int(bloque)*gak)%q))

    return c_bloques


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


# funcion que descifra los bloques de un mensaje aplicando la formula m = c*g^-ak mod q
def descifrar(c_bloques, gak, q):
    m_bloques = []

    # Hallamos el inverso modular de gak respecto a q
    inverso = modinv(gak, q)

    for bloque in c_bloques:
        m_bloques.append(str((int(bloque)*inverso)%q))

    return m_bloques






def main():
    mensaje = "HOLABUENOSDIAS"
    q = seleccion_primo()

    g = int(input(f"Introduzca el número q. Recuerde que debe ser menor que {q}\n"))
    while g<0 or g>q:
        g = int(input("Introduzca el número g: "))

    # obtenemos las claves publicas y la clave compartida
    clave_publica_emisor, clave_publica_receptor, gak = obtener_claves(q, g)

    # convertimos el mensaje a números y preparamos los bloques de tamaño q-1
    m_trans = TexttoNumber(mensaje)
    m_bloques = preparenumcipher(m_trans, q)

    print(f"La clave pública del emisor es: {clave_publica_emisor}")
    print(f"La clave pública del receptor es: {clave_publica_receptor}")

    # ciframos los bloques
    bloques_cifrados = cifrar(m_bloques, gak, q)

    print(f"Los bloques cifrados son: {bloques_cifrados}")

    # desciframos los bloques
    bloques_descifrados = descifrar(bloques_cifrados, gak, q)
    print(f"Los bloques descifrados son: {bloques_descifrados}")

    # completamos los bloques con 0s si es necesario
    bloques = []
    for bloque in bloques_descifrados:
        while len(str(bloque)) < len(str(q))-1:
            bloque = "0" + bloque
        bloques.append(bloque)

    # concatenamos los bloques
    mensaje_descifrado = preparetextdecipher(bloques)

    # eliminamos los 30s finales 
    while mensaje_descifrado[-2:] == "30":
        mensaje_descifrado = mensaje_descifrado[:-2]

    # pasamos el mensaje numerico a texto
    mensaje_descifrado = NumberToText(mensaje_descifrado)
    print(f"El mensaje descifrado es: {mensaje_descifrado}")




if __name__ == "__main__":
    main()