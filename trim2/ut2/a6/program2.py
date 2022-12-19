# Función que muestra un diccionario ordenado
# Lo que hacemos es pasarle el diccionario por parametro
# Luego creamos una variable vacia para formatear el diccionario
# Recorremos el diccionario por claves 
#Añadimos cada clave a la variable vacia y también añadimos el valor de cada una de las claves


def show_contacts(phone_book):
    formatear = ''
    for i in phone_book.keys():
        formatear += f'{i}: {str(phone_book[i])}\n'
        
    return formatear


# Función que añade el nombre y número al diccionario
# Lo que hace es pasarle por parametro el diccionario , nombre y número de telefono
# Esta función lo unico que hace es añadir al diccionario con sus respectivos campos

def add_contact(phone_book,name,phone):
    phone_book[name] = phone
    

# Función que elimina del diccionario
# Lo que hace es pasarle por parametro el diccionario y el nombre
# Si el nombre no esta en el diccionario salta un erro
# Como podemos ver usamos un metodo get con el nombre para obtener el dicho nombre del diccionario y usamos un if no para indicar que no esta en ese diccionario
# Si exite pues lo eliminamos del diccionario usando del 

def remove_contact(phone_book,name):
    if not phone_book.get(name):
        return 'Error - Nombre no exite'
    else:
        del phone_book[name]


# Función que que realiza todo el menu y crea el diccionario
# Creamos un diccionario con algunos datos
# Luego creamos un bucle while para que nos pregunte todo el rato sobre lo que queremos hacer
# Creamos una variable option que es la que indicara cada una de las opciones preguntadas
# Y dependiento de la opciones hara una accion o otra

def menu():
    phone_book = {
        "Alicia" : 645617432,
        "Manuel" : 691854321,
        "Pepe" : 676298911,
        "Zeben" : 699812345
        }
    while True:
        print('1.Mostrar lista de contactos.')
        print('2.Añadir contacto (nombre y teléfono).')
        print('3.Borrar contacto (nombre).')
        print('4.Salir.')
        option = input('Elige un número: ')
        if option == '1':
            print(show_contacts(phone_book))
        elif option == '2':
            name = input('Dame un nombre: ')
            # Esto lo añadimos aqui ya que queria preguntar primero si el nombre exite en vez de tener que preguntar por el nombre y telefono
            if name in phone_book:
                print('Error - Nombre ya exite')
            else:
                phone = int(input('Dame un número de telefono: '))
                print(add_contact(phone_book,name,phone))
        elif option == '3':
            name = input('Dame un nombre: ')
            print(remove_contact(phone_book,name))
        elif option == '4':
            break
        else:
            print("Unknown option")


# Creamos un controlo de excepciones por si da algun error al introducir datos que no debiamos 

try:
    menu()
except:
    print('Error has realizado algo que no debias')





        