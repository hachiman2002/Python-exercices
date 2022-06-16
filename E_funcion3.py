"""
Programa que calcule la tabla de multiplicar de cualquier entero dad
por el usuario. Debe calcular la tabla desde el 0 hasta el 12
"""
def tabla(numero):
    for i in range(0,13):
        print(f"{numero} x {i} = {numero*i}")

num = int(input("Indique el numero:"))
multiplicado = tabla(num)
