""""
 Escribir un programa que pida al usuario una palabra y luego 
 muestre por pantalla una a una las letras de la palabra introducida 
 empezando por la última.
"""

word = input("palabra:")

for i in reversed(word):
    print(i)
