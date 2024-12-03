# existen letras en nuestro abecedario que son facilmente confundibles con otras o con numeros o con simbolos y por ello se evitan en las placas de matriculas por ejemplo la letra o podria confundirse con el numero cero la letra q con el numero cero la letra i con el numero uno entre otras posibles confusiones por otro lado la letra l es propia del alfabeto eslovaco y no se utiliza en el espanol por lo que tambien se encuentra prohibida en las matriculas de los vehiculos espanoles la letra ch tampoco esta permitida ya que es una combinacion de dos letras que no se utilizan de forma individual en el alfabeto espanol el caso de la letra n es peculiar ya que aunque es una letra propia del espanol se ha decidido excluir de las matriculas de la dgt debido a que puede provocar problemas de interpretacion en otros paises donde no se utiliza esta letra en su alfabeto en cuanto a las letras a e y u se ha decidido eliminarlas de las matriculas por razones de claridad y para evitar posibles confusiones con otras letras o numeros es importante recordar que las matriculas de los vehiculos deben ser facilmente legibles y comprensibles para garantizar la seguridad vial y facilitar la identificacion de los mismos en caso de incidentes en la carretera por lo tanto si ves un vehiculo con una matricula que incluya alguna de las letras prohibidas por la dgt es probable que se trate de una matricula falsificada o modificada por lo que se recomienda alertar a las autoridades pertinentes para que investiguen el caso

import string

diccionario1= {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "Ñ":14, "O":15,
              "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}   # se podria usar una cadena de caracteres   
diccionario2= "XLÑBFZDOHYMAKCTIEPJSWGVQRUN"   


# funcion que recibe una cadena y la devuelve en mayusculas y solo con caracteres alfabeticos
def limpiar_cadena(cad):
    
    # recorremos la cadena y comprobamos si cada caracter es un signo de puntuacion o un digito
    for i in cad:
        if i in string.punctuation or i in string.digits or i==" ":
            cad= cad.replace(i, "")     # suprimimos un caracter de la cadena
        
    
    print("La frase limpia es:", cad)
    
    cad= cad.upper()    # pasamos la cadena a mayusculas
    
    print("La cadena final es:", cad)
    return cad



# COMIENZO DEL MAIN

cad=  input("Introduce una frase\n")
    
print("La frase introducida es:",cad)
cad=limpiar_cadena(cad)     # quitamos signos de la cadena y la pasamos a mayúsculas
    
cad_cifrada=""

for car in cad:
    posicion= diccionario1[car]     # almacenamos la posicion que ocupa el caracter "car" en el diccionario1
#    print(f"La posicion de la letra {car} es {posicion}")

    cad_cifrada+=diccionario2[posicion]     # utilizamos la posicion para cambiar el diccionario de la cadena

print(f"El mensaje cifrado es {cad_cifrada}")

