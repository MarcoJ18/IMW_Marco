import sys

def palabra(num,cadena):
    count = 0
    lista = cadena.replace(' ', ',')
    lista = lista.split(',')
    for i in lista:
        if num == len(i):
            count += 1
    if count == 1:
        return f'Hay {count} palabra de tamaño {num}'
    else:
        return f'Hay {count} palabras de tamaño {num}'
    

try:
    k = int(sys.argv[1])
    cadena = sys.argv[2]

    if k < 0:
        print("Es un número negativo")
    else:
        print(palabra(k,cadena))
except:
    print("Es un número inválido")