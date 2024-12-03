import copy

FRECUENCIAS_REALES= {"a":12.53, "c":4.68, "d":5.86, "e":13.68, "i":6.25, "l":4.97, "m":3.15, "n":6.71, "o":8.68, "r":6.87, "s":7.98, "t":4.63}
CAD_FREQ_REAL= "eaosrnidlctumpbgvyqhfzjñxkw"

# FRHSWFCAFWJXSFCCGFSWJIXLFÑFBXJHIPGFSICZXÑHAKFCWFÑICZGCBHLAFSÑICIWJXSIÑICCGKFJISIÑICSHKLIAISUEIJFAAISFFVHWXCFCAXSEAXÑXSBFKXWJHÑGAXSEIJFYFKEAIAXAFWJXIEIBJHXÑICZGCBHJSFÑICFACGKFJIÑFJIAXAFWJXPÑICFACGKFJIÑFJIAXAFWJXHÑICFACGKFJIGCIFCWJFIWJXSEISHLAFSÑICZGSHICFSEIJIWJIAXBIAXAFWJXAFSEJIEHXBFAXAZXLFWIFSAIVXÑIUCISFGWHAHNXFCFAFSEXCIAEIJAIPGFWXKLHFCSFFCÑGFCWJXEJIOHLHBXFCAXSKXWJHÑGAXSBFAISVFOHÑGAISFSEXCIAFSAXAFWJXÑOWXKEIÑIFSWXEFJKHWHBXUXPGFFSGCXÑIKLHCXÑHICBFBISAFWJXSPGFCISFGWHAHNXCBFZIJKXHCBHVHBGXAFCFAXAZXLFWIFSEXCIAFAÑXSIBFAXAFWJXCFSEFÑGAHXJUXPGFXGCPGFFSGCXAFWJXEJIEHXBFAFSEXCIASFOXBFÑHBHBIFRÑAGHJBFAXSKXWJHÑGAXSBFAXBDWBFLHBIXPGFEGFBFEJIVIÑXJEJILAFKXSBFHCWFJEJFWXÑHICFCIWJISEXHSFSBICBFCISFGWHAHNXFSWXAFWJXFCSGXAZXLFWIFCÑGXCWIXAXSAFWJXSXFUGSFOXBFÑHBHBIFAHKHCXJAXSBFAXSKXWJHÑGAXSEIJJXNICFSBFÑAXJHBXBUEXJXFVHWXJEISHLAFSÑICZGSHICFSÑICIWJXSAFWJXSICGKFJISFSHKEIJWXCWFJFÑIJBXJPGFAXSKXWJHÑGAXSBFAISVFOHÑGAISBFLFCSFJZXÑHAKFCWFAFDHLAFSUÑIKEJFCSHLAFSEXJXDXJXCWHNXJAXSFDGJHBXBVHXAUZXÑHAHWXJAXHBFCWHZHÑXÑHICBFAISKHSKISFCÑXSIBFHCÑHBFCWFSFCAXÑXJJFWFJXEIJAIWXCWISHVFSGCVFOHÑGAIÑICGCXKXWJHÑGAXPGFHCÑAGUXXADGCXBFAXSAFWJXSEJIOHLHBXSEIJAXBDWFSEJILXLAFPGFSFWJXWFBFGCXKXWJHÑGAXZXASHZHÑXBXIKIBHZHÑXBXEIJAIPGFSFJFÑIKHFCBXXAFJWXJXAXSXGWIJHBXBFSEFJWHCFCWFSEXJXPGFHCVFSWHDGFCFAÑXSI


#------------------------------------------------------------------------------FUNCIONES---------------------------------------------------------------
def imprimir_frecuencias(arg):
    print("Letra\t|\tFrecuencia")
    for llave, valor in arg.items():
        print(f"{llave}\t|\t{valor}")


def calcular_frecuencias(mensaje_cifrado, frecuencias):
    for letra in mensaje_cifrado:
        frecuencias[letra]=100*(mensaje_cifrado.count(letra))/len(mensaje_cifrado)



def calcular_mayores_frecuencias(frecuencias):
    max_freq=0
    seg_max_freq=0
    letra_max_freq=""
    seg_letra_max_freq=""
    
    # buscamos la letra con la mayor frecuencia de nuestra cadena cifrada
    for llave, valor in frecuencias.items():
        if valor > max_freq:
            max_freq=valor
            letra_max_freq=llave

    print(f"\nLa letra con mayor frecuencia es {letra_max_freq}\n")
    
    for llave, valor in frecuencias.items():
        if valor > seg_max_freq and max_freq > valor:
            seg_max_freq=valor
            seg_letra_max_freq=llave
    print(f"\nLa segunda letra con mayor frecuencia es {seg_letra_max_freq}\n")

    return letra_max_freq, seg_letra_max_freq


def imprimir_menu():
    print("\n\n1. Realizar sustitucion")
    print("2. Restaurar version anterior de la cadena\n")



def realizar_sustitucion(cadena):
    letra_a_sustituir = input("Introduzca la letra que desea sustituir\n").lower()
    letra_sustituta = input("Introduzca la letra por la que deseas sustituirla\n").upper()
    
    # Eliminar la letra sustituta del conjunto de letras disponibles
    historial_frecuencias_reales.append(historial_frecuencias_reales[-1].replace(letra_sustituta.lower(), ""))
    
    # Hacemos una copia profunda de las frecuencias actuales para modificarla
    nuevas_frecuencias = copy.deepcopy(historial_frecuencias[-1])
    
    # Eliminamos la letra sustituida de la copia del diccionario
    nuevas_frecuencias.pop(letra_a_sustituir, None)
    
    # Añadimos esta nueva versión de las frecuencias al historial
    historial_frecuencias.append(nuevas_frecuencias)

    # Coloreamos la letra sustituta en verde y la sustituimos en la cadena
    letra_sustituta_coloreada = "\033[32m" + letra_sustituta + "\033[0m"
    cadena = cadena.replace(letra_a_sustituir, letra_sustituta_coloreada)
        
    return cadena




# cuando sustituimos una letra, debemos eliminarla, pero debemos almacenar historial
def mostrar_sustituciones_sugeridas(letra_max_freq, seg_letra_max_freq, frecuencias_reales):
    print("Sustituciones sugeridas:")
    print(f"\t{letra_max_freq}--->{frecuencias_reales[0]}")
    print(f"\t{seg_letra_max_freq}--->{frecuencias_reales[1]}")



def mostrar_historial(historial):
    for cadena in historial:
        i=1
        print(f"{i}. {cadena}")
        i+=1







#---------------------------------------------------------------------------------MAIN-------------------------------------------------------------------------------
mensaje_cifrado=input("Introduce un mensaje cifrado\n").lower()

# suponemos que el mensaje cifrado esta limpio, en minusculas y sin espacios
frecuencias={}
calcular_frecuencias(mensaje_cifrado, frecuencias)

print(f"\nLas frecuencias del mensaje cifrado son:\n{frecuencias}\n")
    
# tenemos las frecuencias del mensaje cifrado, ahora debemos comparar y sustituir las letras de mayor frecuencia del mensaje con
# las letras que tienen mayor frecuencia en la realidad. Para esto debemos ordenar las frecuencias del mensaje de mayor a menor

tiene_sentido=False
historial_cadenas=[]
historial_frecuencias=[]
historial_frecuencias = [copy.deepcopy(frecuencias)]  # Almacenamos la copia profunda de frecuencias
historial_frecuencias_reales=[]
historial_frecuencias_reales.append(CAD_FREQ_REAL)


while not tiene_sentido:

    historial_cadenas.append(mensaje_cifrado)
    letra_max_freq, letra_seg_max_freq = calcular_mayores_frecuencias(historial_frecuencias[-1])

    imprimir_menu()
    opcion= int(input("Introduzca la opcion que desee\n"))
    if opcion==1:
        print("\n Se va a imprimir el historial de frecuencias\n")
        mostrar_sustituciones_sugeridas(letra_max_freq, letra_seg_max_freq, historial_frecuencias_reales[-1])
        mensaje_semidescifrado=realizar_sustitucion(mensaje_cifrado)
        print(f"El mensaje queda así: {mensaje_semidescifrado}\n\n")
        
        opc=input("¿Tiene sentido el mensaje?\n")
        if opc=="Si" or opc=="si":
            tiene_sentido=True
        else:
            mensaje_cifrado=mensaje_semidescifrado

    elif opcion==2:
        # restaurar version de la cadena anterior
        historial_cadenas.pop()
        mensaje_cifrado=historial_cadenas[-1]
        historial_frecuencias_reales.pop()
        historial_frecuencias.pop()
        print(f"El mensaje es {mensaje_cifrado}")


    else:
        print("Opción no válida")
        exit()



# problema al restaurar la version anterior de la variable frecuencias. No se restaura y la letra eliminada no vuelve.
#  Al borrar una letra de las frecuencias, se borra de todo el historial