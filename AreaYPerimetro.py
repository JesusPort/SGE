# Solicitar al usuario la longitud y el ancho del rectángulo
longitud = float(input("Longitud: "))
ancho = float(input("Ancho: "))

# Calcular el área del rectángulo
area = longitud * ancho

# Calcular el perímetro del rectángulo
perimetro = 2 * (longitud + ancho)

# Mostrar los resultados
print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimetro}")