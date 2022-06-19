"""
Ejercicio 6
Escriba un algoritmo que sume los números ingresados por el usuario hasta que el usuario ingrese
el número 0 (detener las preguntas ante este escenario).
"""
num = int(input("Ingrese numeros:"))
suma = 0
while num != 0:
    suma = suma + num
    num = int(input("Ingrese numeros:"))
print(f"La suma es {suma}")