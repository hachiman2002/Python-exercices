"""
Programa que calcula el IMC de una persona dado su peso y estatura.
Luego indicar su nivel de peso asi:

IMC    CLASIFICACION
-------------------------------------
18,5-24,9 -> normal
25,0-29,9 -> sobrepeso
30,0-34,9 -> obesidad I
35,0-39,9 -> obesidad II
40,0-49,9 -> obesidad III
   > 50   -> obesidad IV

IMC= peso/(estatura*estatura)
"""
def calcularimc(p,a):
    return p / (a * a)

def nivel_peso(imc):
    if imc<18.5:
        return "bajo peso"
    elif imc>=18.5 and imc<=24.9:
        return "Esta normal"
    elif imc>=25.0 and imc<=29.9:
        return "Esta en sobrepeso"
    elif imc>=30.0 and imc<=34.9:
        return "Esta en obesidad I"
    elif imc>=35.0 and imc<=39.9:
        return "Esta en obesidad II"
    elif imc>=40.0 and imc<=49.9:
        return "Esta en obesidad III"
    elif imc>50:
        return"Esta en obesidad IV"
    else:
        return "Digite valores validos"

peso_p = float(input("Peso:"))
estatura = float(input("Estatura:"))

print("Su nivel de peso es:",nivel_peso(calcularimc(peso_p,estatura)))
