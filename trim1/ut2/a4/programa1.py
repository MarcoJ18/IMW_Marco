import sys

letra ='TRWAGMYFPDXBNJZSQVHLCKE'

def dni(num):
    restoD = num % 23
    return f'{num}{letra[restoD]}'


try:

    num = int(sys.argv[1])
    if num < 0:
        print("Es un número negativo")
    elif len(str(num)) > 8:
        print("Deve conter 8 números")
    elif len(str(num)) == 8:
        print(dni(num))
    else:
        print("Deve conter 8 números")
except:
    print("Número inválido")