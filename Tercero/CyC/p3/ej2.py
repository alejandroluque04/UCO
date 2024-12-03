from ej1 import letter2ascii, ascii2letter

# Función que recibe un vector y devuelve 1 si es supercreciente, 0 si es creciente y -1 si no lo es
def knapsack(vector):
    if not vector:
        return -1

    # Si hay algún elemento negativo o cero, no es una mochila
    if any(x <= 0 for x in vector):
        return -1

    total = 0
    # Comprobar si es supercreciente ( el elemento i es <= que la suma de los elementos anteriores)
    for i in range(len(vector)):
        if vector[i] <= total:
            return 0
        total += vector[i]

    return 1



# Función que recibe un valor y una mochila y devuelve la solución al problema de la mochila
def knapsacksol(v, s):      # v es el valor a alcanzar y s es la mochila
    solution = []

    # Se toman los valores que conforman la solucion
    for item in reversed(s):    # empezamos comprobando por el final
        if item <= v:
            v -= item
            solution.append(item)   # los items se van añadiendo en orden inverso

    if v == 0:
        return solution[::-1]   # Se invierte la lista para que esté en el orden correcto
    
    else:
        return []    # Devuelve la solución vacía
    


# Función que recibe un texto y una mochila y devuelve el texto cifrado
def knapsackcipher(texto, mochila):
    # Convertir el texto en una lista de bits
    bits = []
    for char in texto:
        bits.extend(letter2ascii(char))     # usa la función letter2ascii del ejercicio 1
        # al usar extend, se añaden los elementos de la lista devuelta por letter2ascii, no la lista en sí, de forma que bits es una 
        # lista cuyos elementos son los bits de cada caracter del texto, no listas de bits

    # print(f"La lista bits queda asi: {bits}")

    mensaje_cifrado = []
    n = len(mochila)
    
    # Iterar sobre los bits en bloques del tamaño de la mochila
    # Se divide la lista de bits en bloques de tamaño n, y si hace falta, se añaden 0 al final para completar el bloque
    for i in range(0, len(bits), n):
        bloque = bits[i:i+n]
        # print(f"El bloque es: {bloque}")

        # Rellenar con ceros si el bloque es más pequeño que la mochila
        if len(bloque) < n:
            bloque.extend([0] * (n - len(bloque)))

        # Calcular el valor cifrado
        valor_cifrado = sum(b * m for b, m in zip(bloque, mochila))
        mensaje_cifrado.append((valor_cifrado))
    
    return mensaje_cifrado



# Función que recibe un mensaje cifrado y una mochila y devuelve el texto descifrado
def knapsackdecipher(mensaje_cifrado, mochila):
    bits = []

    # Se descifra cada valor del mensaje cifrado
    for valor in mensaje_cifrado:
        solucion = knapsacksol(valor, mochila)  # Se obtiene la solución al problema de la mochila
        bloque_bits = [1 if item in solucion else 0 for item in mochila]    # Se crea un bloque de bits con 1 si el item está en la solución y 0 si no
        bits.extend(bloque_bits)
    
    # Convertir la lista de bits en texto
    texto = ''

    # Iterar sobre los bits en bloques de 8
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]  # Tomar los bits en grupos de 8

        if len(byte) < 8:
            byte.extend([0] * (8 - len(byte)))  # Rellenar con ceros si el byte es más pequeño que 8

        # Como la funcion recibe un string, se convierte la lista de bits a un string de bits y luego se convierte al caracter correspondiente
        char = ascii2letter(''.join(map(str, byte)))  
        texto += char
    
    return texto



def main():
    # tomamos una mochila supercreciente
    mochila_supercreciente = [1, 2, 4, 8, 16]
    texto = "Hola mundo mi nombre es alejandro luque nuñez y estudio la carrera de ingenieria informatica en la universidad de cordoba"

    texto_cifrado = knapsackcipher(texto, mochila_supercreciente)
    print(f"Texto cifrado: {texto_cifrado}\n")

    texto_descifrado = knapsackdecipher(texto_cifrado, mochila_supercreciente)
    print(f"Texto descifrado: {texto_descifrado}")


if __name__ == "__main__":
    main()

