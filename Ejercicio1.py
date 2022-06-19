"""
Ejercicio 1
Escriba un algoritmo que lea del teclado un número entero y que compruebe si el número es menor que 10.
Si no lo está, debe volver a leer el número repitiendo la operación hasta que el usuario escriba un valor correcto.
Finalmente, debe escribir por pantalla el valor leído cuando este sea correcto.
"""
num = int(input("Ingrese numero:"))

while True:
    if num >= 10:
        print("valor correcto")
        break
    else:
        print("Error vuelva a digitar numero")
        num = int(input("Ingrese numero:"))

