"""
Programa que convierte una unidad en dias, horas,minutos
y segundos a segundos
"""
def Convierte(di,ho,min,seg):
    dias_s = di * 86400
    horas_s = ho * 3600
    minutos_s = min * 60
    segundos_s = seg
    total_s = dias_s + horas_s + minutos_s + segundos_s
    return total_s

dias = int(input("Dias:"))
horas = int(input("Horas:"))
minutos = int(input("Minutos:"))
segundo = int(input("Segundos:"))

total_segundos = Convierte(dias,horas,minutos,segundo)

print(total_segundos)

