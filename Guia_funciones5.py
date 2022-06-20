"""
5.- Escribir un programa que, por medio de funciones, represente mediante barra de asteriscos
10 números aleatorios con valores entre 1 y 20
"""
from random import randint
def imprimir():
    for i in range(10):
        aletorio = randint(1,20)
        print("*" * aletorio)

imprimir()