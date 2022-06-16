""""Programa que pida dos numeros al usuario y una operacion a ejecutar
con esos dos numeros las operaciones son:
-suma
-resta(al primero menos el segundo)
-multiplicacion
-division(al primero por el segundo)
-exponenciacion(el primero es la base y el segundo es el exponente)
-radicacion(el primero es el radicando y el segundo es el indice)
"""

def operacion(opc,num1,num2):
    if opc == "suma":
        suma = num1 + num2
        return suma
    elif opc == "resta":
        resta = num1 - num2
        return resta
    elif opc == "multiplicacion":
        multiplicacion = num1 * num2
        return multiplicacion
    elif opc == "division":
        division = num1/num2
        return division
    elif opc == "exponenciacion":
        exponenciacion = num1**num2
        return exponenciacion
    elif opc == "radicacion":
        radicacion = num1 ** (1/num2)
        return radicacion
    else:
        print("Elija un opcion correcta")
print("OPCIONES:suma,resta,multiplicacion,division,exponenciacion,radicacion")
opcion = input("Elije una opcion de operacion:")
opcion = opcion.lower()
n1 = int(input("Numero 1:"))
n2 = int(input("Numero 2:"))

resultado = operacion(opcion,n1,n2)
print(resultado)