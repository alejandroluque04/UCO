from ej2 import knapsack, knapsackcipher
from ej3 import knapsackdeciphermh, modinv, knapsackpublicandprivate
import time

# Funcion que halla una mochila supercreciente a partir de una mochila trampa y el valor de m
def hallar_mochila_supercreciente(mochila_trampa, m):

    # Calcular q, que es el inverso multiplicativo de la primera componente de la mochila trampa
    q = (mochila_trampa[0] * modinv(mochila_trampa[0], m)) % m

    i = 1
    q_list = []

    j=0
    es_supercreciente = False

    while not es_supercreciente:

        tiempo_inicio = time.time() # Iniciar temporizador

        # Calcular la lista de q's
        for _ in range (2**(j*(len(mochila_trampa)+1)) ,2**((j+1)*(len(mochila_trampa)+1))):
            q_list.append((q*i) % m)
            i += 1

        q_list.sort() # Ordenar la lista de q's de menor a mayor


        i = 0

        # Buscar una mochila supercreciente con la lista de q's
        while not es_supercreciente:
            # si no se encuentra una mochila supercreciente, se aumenta el valor de j y se vuelve a calcular la lista de q's
            if i == len(mochila_trampa):
                tiempo_final = time.time() # Finalizar temporizador
                print(f"Tiempo de ejecución: {tiempo_final - tiempo_inicio} segundos\n")
                print(f"No se ha encontrado una mochila supercreciente en el rango [2^{j}*({len(mochila_trampa)}+1), 2^{j+1}*({len(mochila_trampa)}+1)]\n")
                j += 1
                break

            w = mochila_trampa[i] * modinv(q_list[1], m) % m    # Calcular el valor de w

            # Calcular la mochila supercreciente a partir de la mochila trampa y el valor de w
            mochila_supercreciente = []
            for k in range(len(mochila_trampa)):
                mochila_supercreciente.append(mochila_trampa[k] * modinv(w, m) % m)

            # Comprobar si la mochila es supercreciente
            if knapsack(mochila_supercreciente) != 1:
                print("La mochila no es supercreciente\n")
                i += 1
            else:
                tiempo_final = time.time() # Finalizar temporizador
                print(f"Tiempo de ejecución: {tiempo_final - tiempo_inicio} segundos\n")
                return mochila_supercreciente, w




# PASOS:
# 1. Generar pareja de claves publica y mochila trampa (ej3.py -> knapsackpublicandprivate)
# 2. Cifrar un mensaje usando la mochila trampa (ej2.py -> knapsackcipher)
# 3. Aplicar criptoanalisis para hallar la mochila supercreciente (criptoanalisis.py -> hallar_mochila_supercreciente)
# 4. Descifrar el mensaje usando la mochila supercreciente (ej3.py -> knapsackdeciphermh)


def main():
    # tomamos una mochila supercreciente
    mochila_supercreciente = [1, 2, 4, 8, 16]
    
    # Paso 1
    w, m, mochila_trampa = knapsackpublicandprivate(mochila_supercreciente)

    # Paso 2
    texto = input("Introduce el texto a cifrar: \n")
    criptograma = knapsackcipher(texto, mochila_trampa)

    # Paso 3
    mochila_supercreciente_analisis, w_analisis = hallar_mochila_supercreciente(mochila_trampa, m)
    print(f"\nLa mochila supercreciente es: {mochila_supercreciente_analisis}")

    # Paso 4
    print(f"\nCriptograma: {criptograma}")
    mensaje_descifrado = knapsackdeciphermh(mochila_supercreciente_analisis, m, w_analisis, criptograma)

    print(f"\nEl mensaje descifrado es: {mensaje_descifrado}")



if __name__ == "__main__":
    main()