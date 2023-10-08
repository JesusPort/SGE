#Escribe un programa que devuelva si un número dado es primo o no. Para que
#un numero sea primo solo es divisible entre 1 y sí mismo (por ejemplo, 13, 17,
#19…).

# Función para verificar si un número es primo.
def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        #Calcula si en todas las posibles divisiones de un numero el resultado es 0
        if numero % i == 0:
            return False
    return True

# Solicitamos al usuario que ingrese un número.
numero = int(input("Ingrese un número: "))

# Verificamos si el número es primo utilizando la función primo.
if primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
    print("pepe prieto")