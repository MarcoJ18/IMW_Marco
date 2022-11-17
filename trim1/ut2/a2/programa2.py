import sys
import math

try:

#Punto de inicio
    x1 = float(sys.argv[1])
    y1 = float(sys.argv[2])


#Puntos cual de los dos es más cercano
    x2 = float(sys.argv[3])
    y2 = float(sys.argv[4])
    x3 = float(sys.argv[5])
    y3 = float(sys.argv[6])

#Realizamos el calculo
    d1 = (math.sqrt((x1-x2)**2+(y1-y2)**2))
    d2 = (math.sqrt((x1-x3)**2+(y1-y3)**2))
    
#Comprobamos el resultado entre los dos para ver cual es mayor
    if d1 < d2:
        print(f'El punto más cercano es ({int(x2)},{int(y2)}) y está a una distancia de {d1}')
    else:
        print(f'El punto más cercano es ({int(x3)},{int(y3)}) y está a una distancia de {d2}')



except:
    print("No has puesto ningun argumento")