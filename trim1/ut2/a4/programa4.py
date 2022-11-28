import sys

def media(n):
    resultado = 0

    for i in range(1,n+1):
        num = float(sys.argv [i])
        resultado += num

    media = resultado / n

    return f'La media de los valores es: {media}'

try:
    n = len(sys.argv[1:])

    if n < 0:
        print('Es un número negativo')
    else:
        print(media(n))    
except:
    print('Número no valido')

