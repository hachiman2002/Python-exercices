"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""
n = int(input("Ingrese un numero: "))
i = 2
while n % i != 0:
    i += 1
    if i %n == 0:
        print("Es numero primo")
        break
    else:
        print("No es numero primo")
