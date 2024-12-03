import string
from math import gcd


diccionario1= {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "Ñ":14, "O":15,
              "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}   # se podria usar una cadena de caracteres   
diccionario2="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


# funcion que realiza el algoritmo de Euclides sobre dos elemetos que recibe como parametros. Devuelve el MCD y comprueba que los
# dos elementos son apropiados para el algoritmo (son coprimos de 27)

# Función algeucl (determinamos si existe inverso)
def algeucl(p, n=27):
    return gcd(p, n)
    


# Función para calcular el inverso de p en Z_n
def invmod(p, n=27):
    if algeucl(p, n) != 1:
        return None  # Si no existe el inverso, retorna None
    
    # Algoritmo extendido de Euclides para encontrar el inverso
    inverso, inverso_candidato = 0, 1   
    dividendo, divisor = n, p   
    
    while divisor != 0: 
        cociente = dividendo // divisor 
        inverso, inverso_candidato = inverso_candidato, inverso - cociente * inverso_candidato  # actualizamos los valores de inverso y inverso_candidato
        dividendo, divisor = divisor, dividendo - cociente * divisor    # actualizamos los valores de dividendo y divisor
    
    # Asegurarse de que el inverso esté en el rango [0, n-1]
    if inverso < 0:
        inverso = inverso + n
    
    return inverso



# dado un valor n devuelve una lista con todos los elementos que tienen inverso en Zn
def eulerfun(n):
    lista=[]
    for i in range(n):
        if algeucl(i, n)==1:
            lista.append(i)

    return lista




# esta funcion recibe una cadena como argumento, la limpia y la convierte en una cadena numerica en Z27
def TexttoNumber(cad):
    # limpiamos la cadena
    for i in cad:
        if i in string.punctuation or i in string.digits or i==" ":
            cad= cad.replace(i, "")     # suprimimos un caracter de la cadena
            
    cad= cad.upper()
    
    # mostramos la cadena limpia
    # print("La cadena final es:", cad)
    
    # convertimos la cadena en una lista de numeros
    nueva_cadena=[]
    for letra in cad:
        nueva_cadena.append(diccionario1[letra])

    # print(f"La cadena convertida a numeros es {nueva_cadena}")

    return nueva_cadena



# con esta funcion hacemos la transformacion del valor que tiene cada caracter en el texto a un nuevo valor con la funcion f(x)=k*x+d
# donde k debe ser coprimo con 27
def transformacion(k, d, x):
    y = k*x+d

    y= y%27 # nos asegura que el valor de y este en el rango [0, 26]

    # print(f"x={x}\t y={y}\t d={d}\t k={k}")

    y=diccionario2[y]   # convertimos el valor numerico en una letra

    return y



# funcion que comprueba si los valores de k y d son adecuados para el cifrado, y si lo son realiza la transformacion y cifra el mensaje
def Afincypher(mensaje, k, d):
    # comprobamos si los valores de k y d son adecuados para el cifrado, k debe ser coprimo con 27
    son_adecuados= True if algeucl(k, 27)==1 else False
    if not son_adecuados:
        print(f"Los valores {k} y {d} no son validos para el cifrado\n")
        exit()
    
    # convertimos el mensaje en una lista de numeros
    texto_en_numeros = TexttoNumber(mensaje)
    texto_cifrado=[]
    
    # realizamos la transformacion de cada elemento de la lista obteniendo el texto cifrado en una lista
    for elemento in texto_en_numeros:
        texto_cifrado.append(transformacion(k, d, elemento))
    
    # convertimos la lista en una cadena
    # print(f"El texto cifrado es {texto_cifrado}")
    cadena_cifrada=""
    for letra in texto_cifrado:
        cadena_cifrada+=letra
    
    print(f"\nLa cadena cifrada es {cadena_cifrada}")

    return cadena_cifrada



# con esta funcion hacemos la transformacion inversa del valor que tiene cada caracter en el texto a un nuevo valor con la funcion f(x)=k^-1*(y-d)
def inv_transformacion(k, d, y):
    x = invmod(k) * (y-d)
    x= x%27

    x= diccionario2[x]
    return x



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


#---------------------------------------------------------MAIN-------------------------------------------------------------------------
def main():
    mensaje=input("Introduce un mensaje\n")
    k= int(input("Introduce el numero k\n"))
    d= int(input("Introduce el numero entre 0 y 25\n"))
    d= d%27
    Afincypher(mensaje, k, d)

    mensaje=input("Introduce un mensaje para descifrar\n")
    print(f"\nLa cadena descifrada es {afindecypher(mensaje, k, d)}")
    


if __name__ == "__main__":
    main()


# EJEMPLO DE USO
# Hola mi nombre es Alejandro Luque estudio ingenieria informatica en la universidad de cordoba en la provincia de cordoba en andalucia que esta dentro de españa en el continente cuyo nombre es europa
# k=4, d=7
# INXHBMFNBLYWWCHXWPHFSYNXKUKWWCGKSMNMFEWFMWYMHMFANYBHGMOHWFXHKFMÑWYCMSHSSWONYSNLHWFXHQYNÑMFOMHSWONYSNLHWFHFSHXKOMHUKWWCGHSWFGYNSWWCQHJHWFWXONFGMFWFGWOKZNFNBLYWWCWKYNQH
