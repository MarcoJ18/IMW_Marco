import sys


def sumaCuadrados(num):
    resultado = 0
    for i in range(1,num+1):
        cal = i ** 2
        resultado += cal
    
    return resultado

try:
    input = int(sys.argv[1])
    if input < 0:
        print("Es un número negativo")
    else:
        print(sumaCuadrados(input));
except:
    print("No es un número")