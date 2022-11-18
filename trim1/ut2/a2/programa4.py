import sys
import math
import colorama
from colorama import Fore

def diametro(r):
    return f'Diámetro: {int(2*r)}'

def circurferecia(r):
    return f'Perímetro: {2 * math.pi * r}'
    
def circulo(r):
    return f'Área: {math.pi * r**2}'
    

try:
    radio = float(sys.argv[1])


    opcion = 0
    


    while True:

        print(Fore.WHITE + "(1) Calcular el diámetro de la circunferencia:")
        print("(2) Calcular el perímetro de la circunferencia:")
        print("(3) Calcular el área del círculo:")
        print("(4) Salir")

        opcion = int(input("Elige la opcion: "))
        if opcion == 1:
            print(Fore.RED + diametro(radio))
            continue
        elif opcion == 2:
            print(Fore.RED + circurferecia(radio))
            continue
        elif opcion == 3:
            print(Fore.RED + circulo(radio))
            continue
        elif opcion == 4:
            print(Fore.RED + 'Saliendo...')
            break
        else:
            print(Fore.RED + "Error: Unknown opcion")

except:
    print(Fore.RED + "No has puesto ningun argumento o no es valida la opcion")


