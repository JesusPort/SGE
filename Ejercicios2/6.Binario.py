#Escribe un programa que dado un número decimal (en base 10), entre 0 y 15,devuelva el valor equivalente en sistema de numeración binario (en este caso,
#un numero binario de 4 dígitos, completando con ceros a la izquierda si es necesario). Es aconsejable que los dígitos binarios sean una cadena, para
#poder concatenar entre sí. Por ejemplo, si introducimos un 7, nos devolverá 0111. Si se introduce un numero menor que 0 o mayor que 16, nos mostrara un mensaje de error.

#Definimos
def decimal_a_binario(decimal):
    if 0 <= decimal <= 15:
        binario = ""
        for _ in range(4):  # Queremos 4 dígitos binarios
            binario = str(decimal % 2) + binario
            decimal = decimal // 2
        return binario
    else:
        return "Número fuera de rango"

# Solicitar al usuario el número decimal
numero_decimal = int(input("Introduce un número decimal entre 0 y 15: "))

# Convertir y mostrar el número binario
resultado = decimal_a_binario(numero_decimal)
print(f"El número binario es: {resultado}")
