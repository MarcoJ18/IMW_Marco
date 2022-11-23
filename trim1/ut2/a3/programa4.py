import sys


try:
    num = int(sys.argv[1])
    if num < 0:
        print("Es un número negativo")
    else:
        resultado=1
        for i in range(1,num+1):
            resultado *= i
            print(f'{i}! = {resultado}')
except:
    print('No es un número')