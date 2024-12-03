# Programa que realiza el análisis de frecuencia de un mensaje cifrado con el cifrado afín, que mediante dos sustituciones recomendadas
# por el análisis de frecuencia, se calculan los valores de k y d que corresponden a la sustitución y se descifra el mensaje con esos valores.
import copy
from cifrado_afin import invmod
from analisis_afin import calcular_frecuencias, calcular_mayores_frecuencias, imprimir_menu, mostrar_sustituciones_sugeridas, mostrar_comparacion_frecuencias, afindecypher

# Frecuencias individuales de letras
FRECUENCIAS_REALES = {"a":12.53, "c":4.68, "d":5.86, "e":13.68, "i":6.25, "l":4.97, "m":3.15, "n":6.71, "o":8.68, "r":6.87, "s":7.98, "t":4.63}
CAD_FREQ_REAL = "eaosrnidlctumpbgvyqhfzjñxkw"

diccionario1= {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "Ñ":14, "O":15,
              "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}   # se podria usar una cadena de caracteres   
diccionario2="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"



# Función para realizar la sustitución de dos letras en el texto cifrado, calcular los valores de k y d que corresponden a la sustitución
# y descifrar el texto con esos valores
def realizar_sustitucion(texto_cifrado, letra_cifrada1, letra_descifrada1, letra_cifrada2, letra_descifrada2):
    # Calcular k y d a partir de las dos sustituciones
    k, d= guesskd(letra_cifrada1, letra_descifrada1, letra_cifrada2, letra_descifrada2)

    # Descifrar el texto con los valores de k y d calculados
    texto_descifrado= afindecypher(texto_cifrado, k, d)

    print(f"El texto descifrado es {texto_descifrado}") 
    
    respuesta= input("El texto descifrado tiene sentido? (si/no)\n")
    if respuesta=="si":
        return texto_descifrado
    else:
        return None


        
# Función para calcular los valores de k y d a partir de dos sustituciones
def guesskd(letra_cifrada1, letra_descifrada1, letra_cifrada2, letra_descifrada2):
    x1= diccionario1[letra_cifrada1]
    y1= diccionario1[letra_descifrada1]

    x2= diccionario1[letra_cifrada2]
    y2= diccionario1[letra_descifrada2]

    # Calculamos k con la formula y1-y2 = k(x1-x2) mod 27
    k = (y1 - y2) * invmod(x1 - x2) % 27

    # Calculamos d con la formula d= (y1 - k * x1) mod 27
    d= (y1 - k * x1) % 27

    print(f"El valor de k es {k} y el valor de d es {d}:\n")
    return k, d



# Función para realizar el análisis de frecuencia de un mensaje cifrado con el cifrado afín
def afincriptoanalisis():
    mensaje_cifrado= input("Introduzca el mensaje cifrado\n")

    frecuencias = {}
    calcular_frecuencias(mensaje_cifrado, frecuencias)  
    print(f"\nLas frecuencias del mensaje cifrado son:\n{frecuencias}\n")

    tiene_sentido = False
    frecuencias_reales = copy.deepcopy(CAD_FREQ_REAL)


    while not tiene_sentido:
        letra_max_freq, letra_seg_max_freq = calcular_mayores_frecuencias(frecuencias) # Calculamos las frecuencias para mostrar las sugerencias

        imprimir_menu()
        opcion = int(input("Introduzca la opcion que desee\n"))

        # Se va a realizar una sustitucion
        if opcion == 1:
            print("\nSe va a imprimir el historial de frecuencias\n")
            mostrar_sustituciones_sugeridas(letra_max_freq, letra_seg_max_freq, frecuencias_reales)

            print("\nSe va a hacer una doble sustitucion\n")


            letra_cifrada1 = input("Introduzca la letra que desea sustituir\n").upper()
            letra_descifrada1 = input("Introduzca la letra por la que deseas sustituirla\n").upper()
            letra_cifrada2 = input("Introduzca la letra que desea sustituir\n").upper()
            letra_descifrada2 = input("Introduzca la letra por la que deseas sustituirla\n").upper()
            
            mensaje_descifrado = realizar_sustitucion(mensaje_cifrado, letra_cifrada1, letra_descifrada1, letra_cifrada2, letra_descifrada2)

            if mensaje_descifrado is not None:
                print(f"El mensaje descifrado es {mensaje_descifrado}")
                tiene_sentido = True
            else:
                print("No se ha encontrado un mensaje que tenga sentido\n")
                frecuencias_reales=frecuencias_reales.replace(letra_descifrada2.lower(), "")

        # Se va a mostrar la comparacion de frecuencias
        elif opcion == 2:
            mostrar_comparacion_frecuencias(frecuencias, frecuencias_reales)

        # Se va a mostrar los posibles valores de k y d
        elif opcion == 3:
            mostrar_sustituciones_sugeridas(letra_max_freq, letra_seg_max_freq, frecuencias_reales)

            letra_cifrada1_ = input("Introduzca la letra que desea sustituir\n").upper()
            letra_descifrada1_ = input("Introduzca la letra por la que deseas sustituirla\n").upper()
            letra_cifrada2_ = input("Introduzca la letra que desea sustituir\n").upper()
            letra_descifrada2_ = input("Introduzca la letra por la que deseas sustituirla\n").upper()
            guesskd(letra_cifrada1_, letra_descifrada1_, letra_cifrada2_, letra_descifrada2_)

        # Se va a restaurar la cadena de frecuencias reales
        elif opcion == 4:
            print("Restaurando sugerencias anteriores\n")
            frecuencias_reales = letra_descifrada2.lower() + frecuencias_reales

        # Se va a salir del programa
        elif opcion == 5:
            print("Saliendo del programa")
            exit()

        else:
            print("Opcion no valida\n")
            exit()
            

# --------------------------------------------------------------MAIN---------------------------------------------------------------------
def main():
    afincriptoanalisis()


if __name__ == "__main__":
    main()


