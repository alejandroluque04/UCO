# Programa que realiza un analisis de frecuencias sobre un mensaje cifrado con el cifrado afin y trata de descifrarlo usando 
# una sustitucion, mostrando los posibles mensajes que se generarían con los posibles valores de k y d que se pueden obtener
import copy
from cifrado_afin import  eulerfun, TexttoNumber

# Frecuencias individuales de letras
FRECUENCIAS_REALES = {"a":12.53, "c":4.68, "d":5.86, "e":13.68, "i":6.25, "l":4.97, "m":3.15, "n":6.71, "o":8.68, "r":6.87, "s":7.98, "t":4.63}
CAD_FREQ_REAL = "eaosrnidlctumpbgvyqhfzjñxkw"

diccionario1= {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "Ñ":14, "O":15,
              "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}   # se podria usar una cadena de caracteres   
diccionario2="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


# funcion que calcula las frecuencias de las letras en el mensaje cifrado
def calcular_frecuencias(mensaje_cifrado, frecuencias):
    for letra in mensaje_cifrado:
        frecuencias[letra] = 100 * (mensaje_cifrado.count(letra)) / len(mensaje_cifrado)


# funcion que calcula las dos letras con mayor frecuencia en el mensaje cifrado
def calcular_mayores_frecuencias(frecuencias):
    max_freq = 0
    seg_max_freq = 0
    letra_max_freq = ""
    seg_letra_max_freq = ""
    
    # Buscar la letra con mayor frecuencia
    for llave, valor in frecuencias.items():
        if valor > max_freq:
            max_freq = valor
            letra_max_freq = llave

    print(f"\nLa letra con mayor frecuencia es {letra_max_freq}\n")
    
    # Buscar la segunda letra con mayor frecuencia
    for llave, valor in frecuencias.items():
        if valor > seg_max_freq and max_freq > valor:
            seg_max_freq = valor
            seg_letra_max_freq = llave
    print(f"\nLa segunda letra con mayor frecuencia es {seg_letra_max_freq}\n")

    return letra_max_freq, seg_letra_max_freq



# funcion que imprime el menu de opciones
def imprimir_menu():
    print("\n\n1. Realizar sustitucion")
    print("2. Mostrar comparacion de frecuencias")
    print("3. Mostrar posibles valores de k y d")
    print("4. Restaurar sugerencias anteriores\n")
    print("5. Salir\n")



# funcion que muestra las sustituciones sugeridas
def mostrar_sustituciones_sugeridas(letra_max_freq, seg_letra_max_freq, frecuencias_reales):
    print("Sustituciones sugeridas:")
    print(f"\t{letra_max_freq}--->{frecuencias_reales[0]}")
    print(f"\t{seg_letra_max_freq}--->{frecuencias_reales[1]}")



# funcion que transforma el valor de una letra en una letra cifrada segun la ecuaion de cifrado afin y= kx+d mod 27, dependiendo de los valores de k y d
def inv_transformacion(k, d, x):
    y = k*x+d

    y= y%27

    y=diccionario2[y]

    return y


# no podemos importar esta funcion desde cifrado_afin.py porque tomaria la funcion inv_transformacion de ese archivo, y no la que se ha
# definido aqui, ya que son distintas
# funcion que descifra el mensaje cifrado invirtiendo la transformacion realizada en el cifrado
def afindecypher(texto_cifrado, k, d):
    # convertimos el mensaje cifrado en una lista de numeros
    texto_en_numeros = TexttoNumber(texto_cifrado)
    texto_descifrado=[]
    
    # realizamos la transformacion inversa de cada elemento de la lista obteniendo el texto descifrado en una lista
    for elemento in texto_en_numeros:
        texto_descifrado.append(inv_transformacion(k, d, elemento))
        
    cadena_descifrada=""
    # convertimos la lista en una cadena
    for letra in texto_descifrado:
        cadena_descifrada+=letra
    
    return cadena_descifrada




# funcion que realiza la sustitucion de una letra por otra en el mensaje cifrado
def realizar_sustitucion(texto_cifrado, letra_cifrada, letra_descifrada, numeros_con_inverso):
    # en lugar de sustituir la letra en el texto, vamos a calcular los valores para k y d que corresponden a la sustitucion
    # y vamos a descifrar el texto con esos valores
    x= diccionario1[letra_cifrada]
    y= diccionario1[letra_descifrada]
    
    opciones_validas=[] # almacenamos los textos descifrados, apara recuperar el mensaje que tenga sentido mas adelante
    i=1

    # para cada valor de k, calculamos el valor de d y desciframos el texto
    for k in numeros_con_inverso:
        d = (y - k * x) % 27
        print(f"x={x}\t y={y}\t d={d}\t k={k}")
        opciones_validas.append(afindecypher(texto_cifrado, k, d))
        print(f"{i}. El texto descifrado es {opciones_validas[-1]}\n")
        i+=1
    
    respuesta= input("Alguno de los textos descifrados tiene sentido? (si/no)\n")
    if respuesta=="si":
        num_respuesta= int(input("Introduzca el numero del texto que tiene sentido\n")) -1  # recuperamos el texto que tiene sentido
        return opciones_validas[num_respuesta]  # devolvemos el texto que tiene sentido
    else:
        return None
    


# funcion que muestra la comparacion de las frecuencias de las letras en el mensaje cifrado con las frecuencias reales
def mostrar_comparacion_frecuencias(frecuencias_cifrado):
    # Ordenar las letras del mensaje cifrado por frecuencia de mayor a menor
    letras_cifrado_ordenadas = sorted(frecuencias_cifrado.keys(), key=lambda letra: frecuencias_cifrado[letra], reverse=True)

    # Ordenar las letras reales por frecuencia según la constante FRECUENCIAS_REALES
    letras_reales_ordenadas = sorted(FRECUENCIAS_REALES.keys(), key=lambda letra: FRECUENCIAS_REALES[letra], reverse=True)

    # Imprimir ambas columnas
    print("\n\nLetras del mensaje cifrado\t|\tLetras reales")
    print("--------------------------------|---------------------------------")

    # Obtener el número de letras en frecuencias_cifrado
    num_letras_a_imprimir = len(letras_reales_ordenadas)

    # Mostrar las letras ordenadas lado a lado
    for i in range(num_letras_a_imprimir):
        letra_cifrado = letras_cifrado_ordenadas[i] if i < len(letras_cifrado_ordenadas) else ""
        letra_real = letras_reales_ordenadas[i] if i < len(letras_reales_ordenadas) else ""

        # Obtener las frecuencias desde los diccionarios
        frecuencia_cifrado = frecuencias_cifrado[letra_cifrado] if letra_cifrado else 0
        frecuencia_real = FRECUENCIAS_REALES[letra_real] if letra_real in FRECUENCIAS_REALES else 0

        # Imprimir con formato
        try:
            print(f"{letra_cifrado} ({frecuencia_cifrado:.2f}%)\t\t\t|\t{letra_real} ({frecuencia_real:.2f}%)")
        except ValueError as e:
            print(f"Error al imprimir: {e}")
    print("\n\n")


# funcion que muestra los posibles valores de k y d para una letra cifrada y una letra descifrada
def guesskd(letra_cifrada, letra_descifrada, numeros_con_inverso):
    x= diccionario1[letra_cifrada]
    y= diccionario1[letra_descifrada]

    print(f"Para los valores x={x} e y={y} tenemos las siguientes opciones para k y d:\n")
    for k in numeros_con_inverso:
        d = (y - k * x) % 27
        print(f"d={d}\t\t\t k={k}\n")



# funcion principal que realiza el analisis de frecuencias y trata de descifrar el mensaje
def afincriptoanalisis():
    mensaje_cifrado= input("Introduzca el mensaje cifrado\n")

    frecuencias = {}
    calcular_frecuencias(mensaje_cifrado, frecuencias)  # calculamos las frecuencias de las letras en el mensaje cifrado

    print(f"\nLas frecuencias del mensaje cifrado son:\n{frecuencias}\n")

    tiene_sentido = False
    frecuencias_reales = copy.deepcopy(CAD_FREQ_REAL)   # copiamos la cadena de frecuencias reales para poder restaurarla si es necesario

    # almacenamos los numeros que tienen inverso en Z27 para usarlos como posible valor de k
    numeros_con_inverso=eulerfun(27)

    while not tiene_sentido:
        letra_max_freq, letra_seg_max_freq = calcular_mayores_frecuencias(frecuencias)

        imprimir_menu()
        opcion = int(input("Introduzca la opcion que desee\n"))

        # Se va a realizar una sustitucion
        if opcion == 1:
            print("\nSe va a imprimir el historial de frecuencias\n")
            mostrar_sustituciones_sugeridas(letra_max_freq, letra_seg_max_freq, frecuencias_reales)


            letra_cifrada = input("Introduzca la letra que desea sustituir\n").upper()
            letra_descifrada = input("Introduzca la letra por la que deseas sustituirla\n").upper()
            mensaje_descifrado = realizar_sustitucion(mensaje_cifrado, letra_cifrada, letra_descifrada, numeros_con_inverso)

            # Si se ha encontrado un mensaje que tenga sentido, se muestra, si no, se eliminan las letras que se han intentado sustituir para no sugerirlas como
            # sustituciones en el futuro con la letra de mayor frecuencia
            if mensaje_descifrado is not None:
                print(f"El mensaje descifrado es {mensaje_descifrado}")
                tiene_sentido = True
            else:
                print("No se ha encontrado un mensaje que tenga sentido\n")
                frecuencias_reales=frecuencias_reales.replace(letra_descifrada.lower(), "")

        # Se va a mostrar la comparacion de frecuencias
        elif opcion == 2:
            mostrar_comparacion_frecuencias(frecuencias, frecuencias_reales)

        # Se va a mostrar los posibles valores de k y d
        elif opcion == 3:
            mostrar_sustituciones_sugeridas(letra_max_freq, letra_seg_max_freq, frecuencias_reales)

            letra_cifrada_ = input("Introduzca la letra cifrada (x)\n").upper()
            letra_descifrada_ = input("Introduzca la letra descifrada (y)\n").upper()
            guesskd(letra_cifrada_, letra_descifrada_, numeros_con_inverso)

        # Se va a restaurar la cadena de frecuencias reales
        elif opcion == 4:
            try:
                if letra_descifrada is not None:
                    print("Restaurando sugerencias anteriores\n")
                    frecuencias_reales = letra_descifrada.lower() + frecuencias_reales
                else:
                    print("No se han hecho sustituciones\n")
            except NameError:
                print("Error: la variable 'letra_descifrada' no existe\n")

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







