# La actividad consiste en hacer un programa Python que procese un texto pasado por línea de comandos:

import sys

# Función que recorrer el texto en busca de vocales  que lo añadimos en un texto plano
# Lo que hace el programa es recorrer dicho texto y su vez recorrer la cadena de vocales
# Cuando las dos coincidan sumar uno por cada vocal a la variable vacia counter

def num_vowels(text):
    volwerls = 'aAeEiIoOuU' 
    counter = 0
    for i in text:
        for j in volwerls:
            if i == j:
                counter += 1
            
    return counter


# Función que recorrer el texto en busca de espacios en blancos
# Lo que hacemos es recorrer el texto y meter una condición que nos diga si hay un espacio en blanco
# Si lo encuentra lo añadimos a un contador vacio cada vez que haya un espacio en blanco

def num_whitespaces(text):
    counter = 0
    for i in text:
        if i == ' ':
            counter += 1
    return counter

# Función que recorrer el texto en busca de digitos
# Lo que hacemos es recorrer el texto y luego recorrer los digititos
# Si texto y los digitos añadidos son iguales pues sumara uno al contador

def num_digits(text):
    digits = '0123456789'
    counter = 0
    for i in text:
        for num in digits:
            if i == num:
                counter += 1
    return counter


# Función que recorrer el texto en busca de palabras
# Lo que hacemos es hacer un split que es una función de python que lo que hace separar por espacios y añadirlo en un array
# Luego contamos dicho array y nos sale el número de palabras ya que no tenemos en cuenta que las palabras están mal escritas


def num_words(text):
    lista = text.split(' ')  
    return len(lista)


# Función que pone el texto en reverso
# Lo que hacemos es recorrer todo el de principio a final por eso la doble :: pero lo hace desde atras hacia delante
# Ejemplo texto[2:8:2] -> recorrer del dos al ocho y del ocho al dos de forma inversa


def reverse(text):
    return text[::-1]


#Función que cuenta la longitud de la cadena
#Python tiene una función interna que realiza esta operación

def length(text):
    return len(text)


# Función que parte por la mitad el texto
# Lo que hacemos es calcular la mitad gracias a la longitud maxima del texto luego convertilo en entero para que no de flotante
# Una vez hecha la operación solamente hay que recorrer el texto de principio hasta la mitad y luego de mitad hasta el final


def halfs(text):
    half = int(len(text) / 2)
    return f'{text[:half]} | {text[half:]}'


# Función que hace que las vocales sean mayusculas
# Lo que hacemos es re correr el texto y vemos si una de las vocales es minuscula
# Si lo es lo convertimos a mayusculas
# Mejorable: No puede usar un bucle para encontrar las vocales ya que se repetia el doble de palabras al intenar añadirla en allWords


def upper_vowels(text):
    volwerls = 'aeiou'
    allWords = ''
    for i in text:
        if i == volwerls[0] or i == volwerls[1] or i == volwerls[2] or i == volwerls[3] or i == volwerls[4]:
            allWords += i.upper()
        else:
            allWords += i
                      
    return allWords


# Función que recorrer el texto y lo ordena por palabras
# Lo que hacemos es separar por palabras y convertilo en un array para luegar usar la función sorted que hace que ordene didchas palabras
#Luego creamos una cadena vacia. Para añadir cada palabra del array en una cadena y asi tenerlo más bonito y ordenado

def sorted_by_words(text):
    lista = text.split(' ')
    ordenar = sorted(text)
    toString = ''
    for i in ordenar:
        toString += ' ' + i    

    return ordenar


# Función que recorre el texto para sabar la longitud de cada palabra
# Primero convertimos la cadena en una lista separado por espacios
# Luego recorremos dicha lista y lo añadimos en la varible num
# Debemos dejar un espacio y tambien hay que formatear a string ya que si no no nos deja concatenar


def length_of_words(text):
    lista = text.split(' ')
    num = ''
    for i in lista:
        num += ' ' + str(len(i))
    return num


if __name__ == '__main__':
    text = sys.argv[1]
    print('Number of vowels:', num_vowels(text))
    print('Number of whitespaces:', num_whitespaces(text))
    print('Number of digits:', num_digits(text))
    print('Number of words:', num_words(text))
    print('Reverse of text:', reverse(text))
    print('Length of text:', length(text))
    print('Halfs of text:', halfs(text))
    print('Text with uppercased vowels:', upper_vowels(text))
    print('Sorted by words:', sorted_by_words(text))
    print('Length of words:', length_of_words(text))