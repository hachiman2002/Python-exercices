"""
Ejercicio 3
Modifique el algoritmo del problema anterior para que cuente las veces que ha leído un
número de teclado y escriba el resultado por pantalla.
"""
cont = 0
num = int(input("Ingrese numero:"))
while True:
    if num>= 0 and num<=20:
        print("valor correcto")
        break
    else:
        print("Error vuelva a digitar numero")
        num = int(input("Ingrese numero:"))
        cont+=1

print(f"Escribio {cont+1} numeros")
