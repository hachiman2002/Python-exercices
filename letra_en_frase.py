"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

palabra = input("palabra:")
letra = input("letra:")

cont = 0 

for i in (palabra):
    if i == letra:
        cont+=1
    else:
        pass

print(cont)
