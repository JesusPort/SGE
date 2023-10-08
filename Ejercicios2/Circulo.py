#Escribe un programa que devuelva el área de un círculo dado su radio.
#Recuerda que para calcular el area, la formula es Π * r^2
import math

#Recogemos el radio dado
print("Escribe el radio del circulo")
radio=int(input())

#Calculamos
resultado = math.pi * radio**2
print(f"el resultado de un circulo de radio {radio} es {resultado}")
