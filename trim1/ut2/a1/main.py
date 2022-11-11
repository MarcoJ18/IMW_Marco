import sys

try:
    num = int(sys.argv[1])
    resto = 0

    if num == 0:
        print('No hay dinero')

    if num < 0:
        print(f'Debes: {num*-1}€')

    if num >= 50:
        print(num // 50, ' billetes de 50€')
        resto = num % 50

    if resto >= 20:
        print(resto // 20,' billetes de 20€')
        resto = num % 20
    elif num < 50 and num >= 20:
        print(num // 20 ,' billetes de 20€')
        resto = num % 20

    if resto >= 10:
        print(resto // 10 , ' billetes de 10€')
        resto = num % 10
    elif num < 20 and num >= 10:
        print(num // 10, ' billetes de 10€')
        resto = num % 10

    if resto >= 2:
        print(resto // 2 ,' monedas de 2€')
        resto = num % 2
    elif num < 10 and num >= 2:
        print(num // 2,' monedas de 2€')
        resto = num % 2

    if resto >= 1:
        print(resto // 1, ' monedas de 1€')
        resto = num % 1
    elif num < 2 and num >= 1:
        print(num // 1, ' monedas de 1€')
        resto = num % 1

except:
    print('Eso no es número')
















