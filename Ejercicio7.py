"""
Ejercicio 7
Escriba un algoritmo que sume los números ingresados por el usuario y cuando la suma sea superior
a 100 deje de pedir números y muestre el total.
"""
suma = 0
while suma<100:
    num = int(input("Ingrese numeros:"))
    suma = suma + num

print(f"La suma es {suma}")