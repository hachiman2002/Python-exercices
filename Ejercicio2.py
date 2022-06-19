"""
Ejercicio 2
Modifique el algoritmo del problema anterior para que, en vez de comprobar que el número sea menor que 10,
compruebe que se encuentre en el rango (0, 20).
"""
num = int(input("Ingrese numero:"))

while True:
    if num >=0 and num<=20:
        print("valor correcto")
        break
    else:
        print("Error vuelva a digitar numero")
        num = int(input("Ingrese numero:"))

