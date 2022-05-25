2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número separados por comas.
"""
num = int(input("num:"))

for i in range (1,num+1):
    if i % 2 == 1:
        print(i,end=",")    ####solucionar!!!
    else:
        pass

