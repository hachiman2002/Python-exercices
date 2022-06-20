"""
6.- Usando funciones, determine que números son “amigos”. Se define un número amigo si el primero es la suma
de los divisores del segundo y viceversa.

Puedes probar con los números 220 y 284, sin amigos pues se cumple que:

•Los divisores de 220 son: 1,2,4,5,10,11,20,22,44,55,110 y la suma es 284
•Los divisores de 284 son: 1,2,4,71,142 y la suma es 220
"""

def amigos(n1,n2):
    suman1 = 0
    suman2 = 0

    for i in range(1,n1):

        if n1%i==0:
            suman1 = suman1 + i

    for i in range(1,n2):
        if n2 % i == 0:
            suman2 = suman2 + i

    if n1 == suman2 or n2==suman1:
        print("son amigos")#solo se imprime el valor, no lo retorno
    else:
        print("no son amigos")


num1 = int(input("Digite el primer numero:"))
num2 = int(input("Digite el segundo numero:"))

amigos = amigos(num1,num2)