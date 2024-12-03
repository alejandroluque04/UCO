from sympy import Matrix
import numpy as np
import random
from cifrado_afin import algeucl, invmod

diccionario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
n = len(diccionario)


# Función para calcular el determinante de una matriz n x n en Z_n
def det(A, n):
    # Casos base para matrices 1x1 y 2x2
    if len(A) == 1:
        return A[0][0] % n
    
    # Caso base para matriz 2x2
    if len(A) == 2:
        return (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % n
    
    # Caso general
    determinant = 0

    # Calcular el determinante de la matriz
    for col in range(len(A)):
        cofactor = (-1) ** col * A[0][col] * det(minor(A, 0, col), n)
        determinant = (determinant + cofactor) % n

    return determinant



# Función para calcular el menor de una matriz (submatriz eliminando fila i y columna j)
def minor(A, i, j):
    return [[A[x][y] for y in range(len(A[x])) if y != j] for x in range(len(A)) if x != i]



# Función para calcular la inversa de una matriz en Z_n
def InvModMatrix(A, n):
    A = np.array(A)     # Convertir a matriz de numpy
    
    if A.shape[0] != A.shape[1]:
        raise ValueError("La matriz debe ser cuadrada.")    # Verificar si la matriz es cuadrada
    
    sympy_matrix = Matrix(A)    # Convertir a matriz de sympy
    determinant = sympy_matrix.det()

    # Verificar si el determinante es coprimo con n
    if algeucl(determinant, n) != 1:
        return None
    
    det_inv = invmod(determinant % n, n)
    
    # Verificar si el determinante es invertible en Z_n
    if det_inv is None:
        return None
    
    # Calcular la matriz adjunta
    adjugate_matrix = sympy_matrix.adjugate()
    inv_matrix = (adjugate_matrix * det_inv) % n    # Calcular la inversa de la matriz

    return (inv_matrix.applyfunc(lambda x: x % n)).tolist()   # Convertir la matriz de sympy a numpy y luego a lista



# Función para convertir texto en vector numérico
def TexttoNumber(cad):
    cad = cad.upper()
    nueva_cadena = [diccionario.index(letra) for letra in cad if letra in diccionario]
    return nueva_cadena



# Generar matriz clave invertible
def generar_matriz_clave(tam_bloq):
    while True:
        matriz = np.array([[random.randint(0, n - 1) for _ in range(tam_bloq)] for _ in range(tam_bloq)])   # Generar matriz aleatoria
        det = int(round(np.linalg.det(matriz)))     # Calcular el determinante de la matriz
        det_mod = det % n
        if det_mod != 0 and invmod(det_mod, n) is not None:   # Verificar si el determinante es invertible en Z_n
            return matriz



# Función para convertir vector numérico a texto
def vector_a_texto(vector):
    return ''.join([diccionario[num % n] for num in vector])



# Cifrado Hill
def cifrar_hill(texto, matriz_clave):
    texto_cifrado = ""
    tam_bloq = matriz_clave.shape[0]

    # Rellenar el texto si no es múltiplo del tamaño de bloque
    while len(texto) % tam_bloq != 0:
        texto += "X"

    print(f"El texto queda asi: {texto}")
    for i in range(0, len(texto), tam_bloq):
        bloque = texto[i:i + tam_bloq]  # Obtener un bloque del texto
        vector_bloque = TexttoNumber(bloque)    # Convertir el bloque a un vector numérico

        # Convertir el vector_bloque a una matriz vertical (columna)
        vector_bloque = np.array(vector_bloque).reshape(-1, 1)

        # Multiplicación de la matriz por el vector del bloque
        vector_cifrado = np.dot(matriz_clave, vector_bloque) % n
        texto_cifrado += vector_a_texto(vector_cifrado.flatten())  # Aplanar para convertir de nuevo a texto

    return texto_cifrado



# Descifrado Hill
def descifrar_hill(texto_cifrado, matriz_clave):
    texto_descifrado = ""
    tam_bloq = matriz_clave.shape[0]
    matriz_clave_inversa = InvModMatrix(matriz_clave, n)    # Calcular la inversa de la matriz clave

    if matriz_clave_inversa is None:
        print("La matriz clave no tiene inversa en Z27 y no se puede descifrar el mensaje.")
        exit()
    
    for i in range(0, len(texto_cifrado), tam_bloq):
        bloque = texto_cifrado[i:i + tam_bloq]
        vector_bloque = TexttoNumber(bloque)

        # Convertir el vector_bloque a una matriz vertical (columna)
        vector_bloque = np.array(vector_bloque).reshape(-1, 1)

        # Multiplicación de la matriz inversa por el vector del bloque
        vector_descifrado = np.dot(matriz_clave_inversa, vector_bloque) % n
        texto_descifrado += vector_a_texto(vector_descifrado.flatten())  # Aplanar para convertir de nuevo a texto

        # Eliminar los X's añadidos
        while texto_descifrado and texto_descifrado[-1] == "X":
            texto_descifrado = texto_descifrado[:-1]

    return texto_descifrado





# MAIN
def main():
    tamano_bloque = int(input("Introduzca un tamaño de bloque\n"))

    # Generar matriz clave
    matriz_clave = generar_matriz_clave(tamano_bloque)
    print(f"Matriz Clave: {matriz_clave}\n")

    # Verificar si la matriz tiene inversa
    while InvModMatrix(matriz_clave, n) is None:
        print("La matriz clave no tiene inversa. Generando una nueva matriz clave...")
        matriz_clave = generar_matriz_clave(tamano_bloque)

    print(f"Matriz Clave válida: {matriz_clave}\n")

    # Texto a cifrar
    texto = input("Introduzca el texto a cifrar:\n").upper()
    # print(f"Texto original: {texto}")

    texto_limpio = ""

    # Limpiamos el texto
    for letra in texto:
        if letra in diccionario:
            texto_limpio += letra

    # print(f"El texto limpio queda asi {texto_limpio}")

    # Cifrar el texto
    texto_cifrado = cifrar_hill(texto_limpio, matriz_clave)
    print(f"\n\nTexto cifrado: {texto_cifrado}\n\n")

    # Descifrar el texto cifrado
    texto_descifrado = descifrar_hill(texto_cifrado, matriz_clave)
    print(f"Texto descifrado:{texto_descifrado}")




if __name__ == "__main__":
    main()