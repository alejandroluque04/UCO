import string

diccionario1= {"A":"00", "B":"01", "C":"02", "D":"03", "E":"04", "F":"05", "G":"06", "H":"07", "I":"08", "J":"09", "K":"10", "L":"11",
               "M":"12", "N":"13", "Ñ":"14", "O":"15", "P":"16", "Q":"17", "R":"18", "S":"19", "T":"20", "U":"21", "V":"22", "W":"23",
               "X":"24", "Y":"25", "Z":"26"}   
diccionario2= {"00":"A", "01":"B", "02":"C", "03":"D", "04":"E", "05":"F", "06":"G", "07":"H", "08":"I", "09":"J", "10":"K", "11":"L",
               "12":"M", "13":"N", "14":"Ñ", "15":"O", "16":"P", "17":"Q", "18":"R", "19":"S", "20":"T", "21":"U", "22":"V", "23":"W",
               "24":"X", "25":"Y", "26":"Z"}


# esta funcion recibe una cadena numerica en Z27 como argumento y la convierte en una cadena de texto
def NumberToText(cadena_numeros):
    # convertimos la cadena en una lista de numeros
    cadena_texto = ''
    for par in range(0, len(cadena_numeros), 2):
        cadena_texto += diccionario2[cadena_numeros[par:par+2]]

    return cadena_texto



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
    cadena_numeros = ''
    for letra in cad:
        cadena_numeros += diccionario1[letra]

    # print(f"La cadena convertida a numeros es {nueva_cadena}")

    return cadena_numeros



def main():
    cadena = input("Introduce la cadena: ")
    cadena_numeros = TexttoNumber(cadena)
    print(f"La cadena convertida a numeros es {cadena_numeros}")

    cadena_texto = NumberToText(cadena_numeros)
    print(f"La cadena convertida a texto es {cadena_texto}")



if __name__ == "__main__":
    main()



# EJEMPLO DE USO:
# CADENA: Hola soy alejandro luque y estudio ingenieria informatica
# CADENA_NUMEROS: 0715110019152500110409001303181511211721042504192021030815081306041308041808000813051518120020080200