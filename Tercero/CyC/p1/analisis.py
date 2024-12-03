import copy

# Frecuencias individuales de letras
FRECUENCIAS_REALES = {"a":12.53, "c":4.68, "d":5.86, "e":13.68, "i":6.25, "l":4.97, "m":3.15, "n":6.71, "o":8.68, "r":6.87, "s":7.98, "t":4.63}
CAD_FREQ_REAL = "eaosrnidlctumpbgvyqhfzjñxkw"

# Bigramas y trigramas más comunes en español
BIGRAMAS_COMUNES = ["de", "la", "en", "el", "es", "qu", "co", "lo", "al", "se"]
TRIGRAMAS_COMUNES = ["que", "los", "con", "las", "por", "una", "del", "los"]

#------------------------------------------------------------------------------FUNCIONES---------------------------------------------------------------
def imprimir_frecuencias(arg):
    print("Letra\t|\tFrecuencia")
    for llave, valor in arg.items():
        print(f"{llave}\t|\t{valor}")


def calcular_frecuencias(mensaje_cifrado, frecuencias):
    for letra in mensaje_cifrado:
        frecuencias[letra] = 100 * (mensaje_cifrado.count(letra)) / len(mensaje_cifrado)


def calcular_mayores_frecuencias(frecuencias):
    max_freq = 0
    seg_max_freq = 0
    letra_max_freq = ""
    seg_letra_max_freq = ""
    
    for llave, valor in frecuencias.items():
        if valor > max_freq:
            max_freq = valor
            letra_max_freq = llave

    print(f"\nLa letra con mayor frecuencia es {letra_max_freq}\n")
    
    for llave, valor in frecuencias.items():
        if valor > seg_max_freq and max_freq > valor:
            seg_max_freq = valor
            seg_letra_max_freq = llave
    print(f"\nLa segunda letra con mayor frecuencia es {seg_letra_max_freq}\n")

    return letra_max_freq, seg_letra_max_freq


def imprimir_menu():
    print("\n\n1. Realizar sustitucion")
    print("2. Restaurar version anterior de la cadena")
    print("3. Mostrar historial")
    print("4. Mostrar comparacion de frecuencias")
    print("5. Salir\n")



def realizar_sustitucion(cadena):
    letra_a_sustituir = input("Introduzca la letra que desea sustituir\n").lower()
    letra_sustituta = input("Introduzca la letra por la que deseas sustituirla\n").upper()
    
    historial_frecuencias_reales.append(historial_frecuencias_reales[-1].replace(letra_sustituta.lower(), ""))
    
    nuevas_frecuencias = copy.deepcopy(historial_frecuencias[-1])
    
    nuevas_frecuencias.pop(letra_a_sustituir, None)
    
    historial_frecuencias.append(nuevas_frecuencias)

    letra_sustituta_coloreada = "\033[32m" + letra_sustituta + "\033[0m"
    cadena = cadena.replace(letra_a_sustituir, letra_sustituta_coloreada)
        
    return cadena


def mostrar_sustituciones_sugeridas(letra_max_freq, seg_letra_max_freq, frecuencias_reales):
    print("Sustituciones sugeridas:")
    print(f"\t{letra_max_freq}--->{frecuencias_reales[0]}")
    print(f"\t{seg_letra_max_freq}--->{frecuencias_reales[1]}")


def calcular_frecuencias_bigramas(mensaje_cifrado):
    bigramas = {}
    for i in range(len(mensaje_cifrado) - 1):
        bigrama = mensaje_cifrado[i:i+2]
        if bigrama in bigramas:
            bigramas[bigrama] += 1
        else:
            bigramas[bigrama] = 1
    return bigramas


def calcular_frecuencias_trigramas(mensaje_cifrado):
    trigramas = {}
    for i in range(len(mensaje_cifrado) - 2):
        trigrama = mensaje_cifrado[i:i+3]
        if trigrama in trigramas:
            trigramas[trigrama] += 1
        else:
            trigramas[trigrama] = 1
    return trigramas


def mostrar_sugerencias_bigramas_trigramas(bigramas, trigramas):
    print("\nSugerencias basadas en bigramas y trigramas:")
    
    # Mostrar sugerencias de bigramas
    for bigrama, _ in sorted(bigramas.items(), key=lambda item: item[1], reverse=True):
        if bigrama in BIGRAMAS_COMUNES:
            print(f"Sugerencia: El bigrama {bigrama} es común en español.")
    
    # Mostrar sugerencias de trigramas
    for trigrama, _ in sorted(trigramas.items(), key=lambda item: item[1], reverse=True):
        if trigrama in TRIGRAMAS_COMUNES:
            print(f"Sugerencia: El trigrama {trigrama} es común en español.")



def mostrar_historial(historial):
    i=1
    for cadena in historial:
        print(f"{i}. {cadena}")
        i+=1



def mostrar_comparacion_frecuencias(frecuencias_cifrado, frecuencias_reales):
    # Ordenar las letras del mensaje cifrado por frecuencia de mayor a menor
    letras_cifrado_ordenadas = sorted(frecuencias_cifrado.keys(), key=lambda letra: frecuencias_cifrado[letra], reverse=True)

    # Ordenar las letras reales por frecuencia según la constante FRECUENCIAS_REALES
    letras_reales_ordenadas = sorted(FRECUENCIAS_REALES.keys(), key=lambda letra: FRECUENCIAS_REALES[letra], reverse=True)

    # Imprimir ambas columnas
    print("\n\nLetras del mensaje cifrado\t|\tLetras reales")
    print("--------------------------------|---------------------------------")

    # Obtener el número de letras en frecuencias_cifrado
    num_letras_a_imprimir = len(letras_cifrado_ordenadas)

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

# Ejemplo de uso
# Asegúrate de que al llamar a esta función, le pases correctamente los diccionarios de frecuencias.





#---------------------------------------------------------------------------------MAIN-------------------------------------------------------------------------------
mensaje_cifrado = input("Introduce un mensaje cifrado\n").lower()

frecuencias = {}
calcular_frecuencias(mensaje_cifrado, frecuencias)

print(f"\nLas frecuencias del mensaje cifrado son:\n{frecuencias}\n")

tiene_sentido = False
historial_cadenas = []
historial_frecuencias = []
historial_frecuencias = [copy.deepcopy(frecuencias)]
historial_frecuencias_reales = []
historial_frecuencias_reales.append(CAD_FREQ_REAL)

while not tiene_sentido:
    historial_cadenas.append(mensaje_cifrado)
    letra_max_freq, letra_seg_max_freq = calcular_mayores_frecuencias(historial_frecuencias[-1])

    imprimir_menu()
    opcion = int(input("Introduzca la opcion que desee\n"))
    
    if opcion == 1:
        print("\nSe va a imprimir el historial de frecuencias\n")
        mostrar_sustituciones_sugeridas(letra_max_freq, letra_seg_max_freq, historial_frecuencias_reales[-1])
        
        # Calcular y mostrar sugerencias basadas en bigramas y trigramas
        # bigramas = calcular_frecuencias_bigramas(mensaje_cifrado)
        # trigramas = calcular_frecuencias_trigramas(mensaje_cifrado)
        # mostrar_sugerencias_bigramas_trigramas(bigramas, trigramas)
        
        mensaje_semidescifrado = realizar_sustitucion(mensaje_cifrado)
        print(f"El mensaje queda así: {mensaje_semidescifrado}\n\n")
        
        opc = input("¿Tiene sentido el mensaje?\n")
        if opc.lower() == "si":
            tiene_sentido = True
        else:
            mensaje_cifrado = mensaje_semidescifrado

    elif opcion == 2:
        historial_cadenas.pop()
        mensaje_cifrado = historial_cadenas[-1]
        historial_frecuencias_reales.pop()
        historial_frecuencias.pop()
        print(f"El mensaje es {mensaje_cifrado}")

    elif opcion==3:
        mostrar_historial(historial_frecuencias)

    elif opcion==4:
        mostrar_comparacion_frecuencias(historial_frecuencias[-1], historial_frecuencias_reales[-1])

    elif opcion==5:
        print("Saliendo...")
        exit()
    else:
        print("Opción no válida")
        exit()


# modificar menu y opciones de menu