import time
import random
from math import gcd

# funcion para comprobar si un número es probablemente primo
def es_primo(n, n_iteraciones):
    while n_iteraciones > (n-3):
        n_iteraciones = n_iteraciones//2

    # le pasamos el test de primalidad de Solovay-Strassen
    valores_de_a = []

    # Caso trivial: si n es menor o igual a 1, no es primo
    if n <= 1 or n % 2 == 0 or n<=3:
        return False

    for _ in range(n_iteraciones): 
        a = random.randint(2, n-1)
        if a not in valores_de_a:
            valores_de_a.append(a)
        else:
            while a in valores_de_a:
                a = random.randint(2, n-1)
            valores_de_a.append(a)

        if gcd(a, n) != 1:
            return False

        if pow(a, n-1, n) != 1:
            return False
        
# le pasamos el test de primalidad de Miller-Rabin
    # Escribir n-1 como 2^s * t, donde d es impar
    s = 0
    t = n - 1
    while t % 2 == 0:
        t //= 2
        s += 1

    
    for _ in range(n_iteraciones):
        a = random.randint(2, n - 2)
        x = pow(a, t, n)  # a^t % n

        # n debe dividir a 2^s * t para ser primo
        if x == 1 or x == n - 1:
            # es primo o pseudo
            return True
            
        else:
            for _ in range(s - 1):
                x = pow(x, 2, n)  # x = x^2 % n
                if x == n - 1:
                    # es primo o pseudo
                    return True
            
            return False

        
    


# funcion para pasar el test de primalidad de Solovay-Strassen a un numero aleatorio dado un rango
def primosolostra(min, max, n_iteraciones):
    tiempo_inicio = time.time()
    n = random.randint(min, max)
    # print(f"Se ha tomado el valor {n}. Vamos a comprobar si es primo\n")

    # queremos almacenar los valores que ya hemos usado para no repetirlos
    valores_de_a = []


    for _ in range(n_iteraciones):
        # tomamos un valor aleatorio entre 2 y el numero que queremos comprobar 
        a = random.randint(2, n-1)

        if a not in valores_de_a:
            valores_de_a.append(a)
        else:
            while a in valores_de_a:
                a = random.randint(2, n-1)
            valores_de_a.append(a)

        # si el mcd de a y n no es 1, no es primo
        if gcd(a, n) != 1:
            tiempo_fin = time.time()
            print("Primosolostra: Tiempo de ejecución:", tiempo_fin - tiempo_inicio)
            # print("El número no es primo")
            return False, n, 0

        # si a^(n-1) mod n no es 1, no es primo
        if pow(a, n-1, n) != 1:
            tiempo_fin = time.time()
            print("Primosolostra: Tiempo de ejecución:", tiempo_fin - tiempo_inicio)
            # print("El número no es primo")
            return False, n, 0
        
        tiempo_fin = time.time()
        print("Primosolostra: Tiempo de ejecución:", tiempo_fin - tiempo_inicio)
        # print(f"El numero es primo con una probabilidad de {1-1/2**n_iteraciones}")
        # print(f"El numero es pseudoprimo con una probabilidad de {0.5**n_iteraciones}")
        return True, n, 0.5**n_iteraciones




# funcion para pasar el test de primalidad de Miller-Rabin a un numero aleatorio dado un rango
def primoMillerRabin(min, max, n_iteraciones):
    tiempo_inicio = time.time()
    n = random.randint(min, max)
    # print(f"Se ha tomado el valor {n}. Vamos a comprobar si es primo\n")


    # Caso trivial: si n es menor o igual a 1, no es primo
    if n <= 1:
        tiempo_fin = time.time()
        print("Miller-Rabin: Tiempo de ejecución:", tiempo_fin - tiempo_inicio)
        # print("El número no es primo")
        return False, n, 0
    
    # Caso trivial: si n es 2 o 3, son primos
    if n <= 3:
        tiempo_fin = time.time()
        print("Miller-Rabin: Tiempo de ejecución:", tiempo_fin - tiempo_inicio)
        return True, n, 0
    
    # Si n es par, no es primo
    if n % 2 == 0:
        tiempo_fin = time.time()
        print("Miller-Rabin: Tiempo de ejecución:", tiempo_fin - tiempo_inicio)
        # print("El número no es primo")
        return False, n, 0

    # Escribir n-1 como 2^s * t, donde d es impar
    s = 0
    t = n - 1
    while t % 2 == 0:
        t //= 2
        s += 1

    for _ in range(n_iteraciones):
        a = random.randint(2, n - 2)
        x = pow(a, t, n)  # a^t % n

        # n debe dividir a 2^s * t para ser primo
        if x == 1 or x == n - 1:
            # es primo o pseudo
            tiempo_fin = time.time()
            print("Miller-Rabin: Tiempo de ejecución:", tiempo_fin - tiempo_inicio)
            # print("El numero es probablemente primo")
            # print(f"Probabilidad de que sea primo: {1-0.25**n_iteraciones}")
            # print(f"Probabilidad de que sea pseudoprimo: {0.25**n_iteraciones}")
            return True, n, 1/4**n_iteraciones
            
        else:
            for _ in range(s - 1):
                x = pow(x, 2, n)  # x = x^2 % n
                if x == n - 1:
                    # es primo o pseudo
                    tiempo_fin = time.time()
                    print("Miller-Rabin: Tiempo de ejecución:", tiempo_fin - tiempo_inicio)
                    # print("El numero es probablemente primo")
                    # print(f"Probabilidad de que sea primo: {1-0.25**n_iteraciones}")
                    # print(f"Probabilidad de que sea pseudoprimo: {0.25**n_iteraciones}")
                    return True, n, 1/4**n_iteraciones


            tiempo_fin = time.time()
            print("Miller-Rabin: Tiempo de ejecución:", tiempo_fin - tiempo_inicio)
            # print("El número no es primo")
            return False, n, 0
        
    

# funcion que nos muestra una lista de primos entre 100 y 1000000 para que seleccionemos uno
def seleccion_primo():
    print("Vamos a seleccionar un primo para generar las claves RSA")
    print("Se van a mostrar una serie de primos recomentados\n")

    # lista donde se almacenarán los primos para evitar recomendaciones repetidas
    lista_primos = []

    # hallamos 5 primos con el test de Miller-Rabin y 5 con el test de Solovay-Strassen. Se hacen 20 iteraciones de cada test
    for _ in range(5):
        es_primo_miller_rabin, es_primo_olostra = False, False

        # mientras no se haya encontrado un primo con el test de Miller-Rabin, se sigue buscando hasta encontrar un primo que no esté en la lista
        while not es_primo_miller_rabin:
            es_primo_miller_rabin, n_primo, prob_pseudoprimo = primoMillerRabin(100, 1000000, 20)
            if es_primo_miller_rabin and n_primo not in lista_primos:
                lista_primos.append(n_primo)
        
        # mientras no se haya encontrado un primo con el test de Solovay-Strassen, se sigue buscando hasta encontrar un primo que no esté en la lista
        while not es_primo_olostra:
            es_primo_olostra, n_primo_olostra, prob_pseudoprimo = primosolostra(100, 1000000, 20)
            if es_primo_olostra and n_primo_olostra not in lista_primos:
                lista_primos.append(n_primo_olostra)

    # mostramos los primos recomendados
    print("Los primos recomendados son:")
    for i in range(len(lista_primos)):
        print(f"\t{i+1}. \t{lista_primos[i]}")

    primo= int(input("Introduce el primo seleccionado: \n"))

    # si el primo no esta en la lista, debemos comprobar que sea primo. El primo debe ser mayor que 100 para facilitar los test
    if primo not in lista_primos:
        if primo < 100:
            print("El número es demasiado pequeño")
            exit()
        if not es_primo(primo, 20):
            print("El número no es primo")
            exit()
    
    return primo



def main():
    es_primo, n_primo, prob_pseudoprimo = primoMillerRabin(100, 1000000, 20)
    if es_primo:
        print(f"El número {n_primo} es primo con una probabilidad de {1-prob_pseudoprimo}")
    else:
        print(f"El número {n_primo} no es primo")

    es_primo, n_primo, prob_pseudoprimo = primosolostra(100, 1000000, 20)
    if es_primo:
        print(f"El número {n_primo} es primo con una probabilidad de {1-prob_pseudoprimo}")
    else:
        print(f"El número {n_primo} no es primo")


if __name__ == "__main__":
    main()