#Preguntar si quiere convertir
print("Si quiere convertir de C a F. Pulse 1")
print("Si quiere convertir de F a C. Pulse 2")

#Guardamos la opcion
opcion = int(input())


temperatura = float(input("Ingrese la temperatura a convertir: "))

if opcion == 1:
    resultado= ((temperatura * 9/5)+32)
    print(resultado)
elif opcion == 2:
    resultado= ((temperatura -32)*5/9)
    print(resultado)
else:
    print("Opcion incorrecta")



