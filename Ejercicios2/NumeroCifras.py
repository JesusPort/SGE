#Escribe un programa que, dado un número entero (este numero no podrá ser
#menor o igual que 0), determine el número de cifras que tiene. Por ejemplo,
#para un 253, devuelve un 3.


#Pedimos un numero
print("Escribe un numero para hallar sus cifras")
numero = int(input())

if numero < 0 :
    print("El numero debe ser positivo")
else:
    cifras=len(str(numero))
    print(f"El numero de cifras de {numero} es {cifras}")

