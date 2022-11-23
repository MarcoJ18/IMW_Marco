import sys

def mcm(a,b):
    if a == 0 or b == 0:
        return 0
    while b != 0:
        cal = b
        b = a % b
        a = cal
    return a
                    

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
if num1 < 0 or num2 < 0:
    print("Es un número negativo")
else:
    print(mcm(num1,num2))