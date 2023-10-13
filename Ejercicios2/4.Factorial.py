#Escribe un programa que devuelva el factorial de un número N (siendo N un
#número entero positivo).

def factorial(n):
    if n < 0:
        return "El numero tiene que ser positivo"

    elif n == 0 :
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

#Pedimos el numero al usuario
print("Escribe el numero para calcular su factorial")
n=int(input())
resultado=factorial(n)
print(f"El resultado del factorial de {n} es: {resultado}")
