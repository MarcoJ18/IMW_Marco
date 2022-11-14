import sys


    
num = float(sys.argv[1])


if num >= 0 and num <= 10:
    if num == 10:
        print('Matrícula de honor')
    elif num >= 9:
        print('Sobresaliente')
    elif num >= 7:
        print('Notable')
    elif num >= 5:
        print('Aprobado')
    else:
        print('Suspenso')
else:
    print('Error')