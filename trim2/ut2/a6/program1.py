import sys

#Creamos una función donde va recorger una sentencia
# Creamos un diccionario vacio y luego dicha sentecia lo separamos por palabras , también creamo un variable para luego formatear el resultado del diccionario
# Recorremos la lista y añadimos la clave que sera de esta forma summary[nombre] y luego le añadimos el valor que nuestro caso usaremos una función que cuenta
# El numero de veces que se repetite dentro de lista:
# Ejemplo : example = [1, 2, 3, 4,2,2,2]
#         : print(example.count(2))
#         : resultado = 4

#Luego de añadir todo en el diccionario lo vamos a formatear
#Para ello vamos a recorrer el diccionario y añadirlo en la variable vacia formatear

def count_words(sentence):
    summary = {}
    lista = sentence.split()
    formatear = ''
    
    for i in lista:
        summary[i] = lista.count(i)
 
    for i in summary.keys():
        formatear += f'{i}: {summary[i]}\n'
    
    return formatear
        



sentence = sys.argv[1]
print(count_words(sentence))

