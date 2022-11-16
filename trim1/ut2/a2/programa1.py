import sys
import math


try:

    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    num3 = float(sys.argv[3])


    def ecuciones(a,b,c):
    
        if b**2 -4*a*c < 0:
            return "No tiene solución real"
        elif a == 0:
            x = -c // b
            return f"x={int(x)}"
        else:
            x1 = (-b+(math.sqrt(b**2 - 4*a*c)))//2*a
            x2 = (-b-(math.sqrt(b**2 - 4*a*c)))//2*a
            return f"x1={int(x1)}; x2={int(x2)}"

    print(ecuciones(num1,num2,num3))

except:
    print("No has puesto ningun argumento")
