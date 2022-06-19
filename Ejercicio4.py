"""
Ejercicio 4
Modifique el algoritmo del problema anterior para que se realicen 5 lecturas por teclado como máximo.

"""
cont = 0
contn = 1
num = int(input("Ingrese numero:"))
while True and contn<5:
    contn+=1
    if num>= 0 and num<=20:
        print("valor correcto")
        break
    else:
        print("Error vuelva a digitar numero")
        num = int(input("Ingrese numero:"))
        cont+=1

print(f"Escribio {cont+1} numeros")

