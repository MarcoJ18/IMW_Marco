import sys

#Ponemos un rango del 2 al input ya que si el resto da 0 en cualquier numero no es primo pero si no da cero pues significa que puede divir por si mismo o uno

def primo(num):
    for i in range(2,num):
        if num % i == 0:
            return "No es primo!"
    
    return "Es primo!"
    

try:
    input = int(sys.argv[1])
    if input < 0:
        print("Es un número negativo")
    else:
        print(primo(input));
except:
    print("No es un número")