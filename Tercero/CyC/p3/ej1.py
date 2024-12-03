# def letter2ascii(letter):
#     return format(ord(letter), '08b')   # ord() devuelve el valor ASCII de un caracter, format() convierte el valor a binario. Retorna string

# funcion que convierte un caracter a su valor ASCII
def letter2ascii(letter):
    return [int(bit) for bit in format(ord(letter), '08b')]     # retorna una lista de int


# funcion que convierte un texto a una lista de valores ASCII
def text2ascii(texto):
    return [letter2ascii(char) for char in texto]   # retorna una lista de listas


# funcion que convierte un valor ASCII a un caracter
def ascii2letter(ascii):
    return chr(int(ascii, 2))   # chr() convierte un valor ASCII a caracter, int() convierte el valor a decimal

# MAIN
# print(letter2ascii('A'))   # 01000001
# print(ascii2letter('01000001'))   # A