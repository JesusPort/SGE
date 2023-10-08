
num1 = int(input("Primer numero "))
num2 = int(input("Segundo numero "))


print("Seleccione una opción:")
print("1. Sumar los dos números")
print("2. Restar el segundo número del primero")


opcion = int(input())


if opcion == 1:
    resultado = num1 + num2
    print(resultado)
elif opcion == 2:
    resultado = num1 - num2
    print(resultado)
else:
    print("Pulse 1 o 2")