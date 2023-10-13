#Vamos a realizar el pequeño juego de adivinar un número entre 0 y 99. El
#usuario realizará sucesivos intentos. En cada uno de ellos, el programa dirá si
#el número secreto es mayor o menor que el introducido, y al acertarlo reflejará
#el número total de intentos.

import random

# Generar un número aleatorio entre 0 y 99 como número secreto
numero_secreto = random.randint(0, 99)

# Inicializar el contador de intentos
intentos = 0

# Iniciar el bucle del juego
while True:
    # Solicitar al usuario que adivine el número
    intento = int(input("Adivina el número (entre 0 y 99): "))

    # Incrementar el contador de intentos
    intentos += 1

    # Comprobar si el intento es correcto
    if intento == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor. Intenta de nuevo.")
    else:
        print("El número secreto es menor. Intenta de nuevo.")
