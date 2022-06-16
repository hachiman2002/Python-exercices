"""Programa que valida si un numero es primo"""

def v_primo(num):
    if num<=1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % 2 == 0:
                return False
        return True

num = int(input("Digite un numero:"))
validar = v_primo(num)
print(validar)