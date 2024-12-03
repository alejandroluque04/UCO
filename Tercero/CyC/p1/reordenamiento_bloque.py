import string
import math

# funcion que recibe una cadena y la devuelve en mayusculas y solo con caracteres alfabeticos
def limpiar_cadena(cad):
    
    # recorremos la cadena y comprobamos si cada caracter es un signo de puntuacion o un digito
    for i in cad:
        if i in string.punctuation or i in string.digits or i==" ":
            cad= cad.replace(i, "")     # suprimimos un caracter de la cadena
        
    
    # print("La frase limpia es:", cad)
    
    cad= cad.upper()
    
    # print("La cadena final es:", cad)
    return cad



# COMIENZO DEL MAIN

cad= input("Introduce una frase\n")
    
print("\nLa frase introducida es:",cad)
cad=limpiar_cadena(cad)

tam_bloq= int(input("\nIntroduzca tamaño de bloque\n"))
n_grupos= math.ceil(len(cad)/tam_bloq)      # ceil redondea siempre a la alza
print(f"\nEl numero de grupos de tamaño {tam_bloq} con la cadena {cad} es {n_grupos}")    # ya tenemos el numero de filas y columnas de la matriz



# ahora debemos coger la palabra para ordenar y cifrar

codigo= input(f"\nIntroduce una palabra de {tam_bloq} letras\n")
if len(codigo) != tam_bloq:
    print("No has introducido una palabra de la longitud correcta")
    exit()

codigo_ordenado= sorted(codigo)     # de esta forma podemos mantener el codigo original

print(f"\nLa clave ordenada es {codigo_ordenado}")



lista=[]

# vamos a agrupar nuestra cadena, tendremos una lista de diccionarios
for i in range(n_grupos):
    lista.append({})                       # creamos un elemento vacio de la lista, que corresponderá a un diccionario

    # la variable lista tendra la siguiente forma: [{},{},...]
    for j in range(tam_bloq):
        if (tam_bloq*i+j) < len(cad):     # comprobamos que estamos dentro de la cadena, sino, nos encontramos en un excedente por redondeo
            lista[i][codigo[j]]=cad[tam_bloq*i+j]
        else:
            lista[i][codigo[j]]="0"         # añadimos caracteres "0" para rellenar los huecos debidos al redondeo

print()
for grupo in lista:
    print(f"Grupo: {grupo}")

# tenemos una lista de diccionarios. Cada diccionario tiene como llaves las letras del codigo y como valores, las letras de nuestro mensaje


mensaje_cifrado= ""

# usamos el codigo ordenado para insertar los valores por filas de los diccionarios de forma ordenada. Hay que tener cuidado ya que 
    # tenemos valores "0" que debemos descartar
for fila in range(n_grupos):
    for letra in codigo_ordenado:       # al usar el codigo ordenado, se desordena nuestro mensaje
        if lista[fila][letra] != "0":
            mensaje_cifrado+= lista[fila][letra]

print(f"El mensaje cifrado es: {mensaje_cifrado}")

