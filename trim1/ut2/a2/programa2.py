import sys
import math

#Punto de inicio
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])


#Puntos cual de los dos es más cercano
num3 = float(sys.argv[3])
num4 = float(sys.argv[4])
num5 = float(sys.argv[5])
num6 = float(sys.argv[6])


def distancia(x1,y1,x2,y2):
    d = (math.sqrt((x1-x2)**2+(y1-y2)**2))
    return d

#Restamos uno por luego se lo vamos a sumar dentro del bucle por si el numero es igual
inicio = (num1+num2)-1
fin1 = num3+num4
fin2 = num5+num6

while True:
    inicio += 1
    if inicio == fin1:
        cercano = f"({int(num3)},{int(num4)})"
        resultado = distancia(num1,num2,num3,num4)
        break
    elif inicio == fin2:
        cercano = f"({int(num5)},{int(num6)})"
        resultado = distancia(num1,num2,num5,num6)
        break





print(f'El punto más cercano es {cercano} y está a una distancia de {resultado}')