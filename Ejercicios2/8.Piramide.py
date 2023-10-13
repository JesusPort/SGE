#Escribe un programa que dibuje una pirámide invertida en pantalla como la de
#la figura. La altura se pasará como parámetro. Si se pasa una altura =0 o
#negativa, la función devolverá un error.
#Ejemplo para altura = 5
# *********
#  *******
#   *****
#    ***
#     *

def dibujar_piramide_invertida(altura):
    if altura <= 0:
        return "La altura debe ser un número positivo mayor que cero"

    for i in range(altura, 0, -1):
        # Imprimir espacios en blanco antes de los asteriscos
        print(" " * (altura - i) + "*" * (2 * i - 1))


altura = int(input("Ingrese la altura de la pirámide: "))
dibujar_piramide_invertida(altura)
