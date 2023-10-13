#Escribe un programa que devuelva el término N (siendo N un número entero
#positivo) de la serie de Fibonacci, esta sigue la siguiente serie: 1, 1, 2, 3, 5, 8,
#13, 21… y así sucesivamente.

def fibonacci(n):
    if n <= 0:
        return "El valor de N debe ser un número entero positivo"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a, b = 1, 1
        i = 3
        while i <= n:
            a, b = b, a + b
            i += 1
        return b

n = int(input("Ingrese el valor de N: "))
resultado = fibonacci(n)
if type(resultado) == int:
    print(f"El término {n} de la serie de Fibonacci es: {resultado}")
else:
    print(resultado)