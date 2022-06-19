"""
Ejercicio 5
Escriba un algoritmo que calcule e imprima la suma de los n primeros números enteros positivos.
El valor de n debe leerse del teclado y ser ingresado por el usuario.
"""
n = int(input("Ingres un numero:"))
suma = 0

for i in range(n+1):
    suma = suma + i
print(f"La suma es {suma}")