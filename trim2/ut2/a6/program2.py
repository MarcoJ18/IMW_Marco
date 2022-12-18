



def show_contacts(phone_book):
    formatear = ''
    for i in phone_book.keys():
        formatear += f'{i}: {str(phone_book[i])}\n'
        
    return formatear

def add_contact(phone_book,name,phone):
    if name in phone_book:
        return 'Error - Nombre ya exite'
    else:
        phone_book[name] = phone
    

def remove_contact(phone_book,name):
    if not phone_book.get(name):
        print('No exite')



def menu():
    phone_book = {
        "Alicia" : 645617432,
        "Manuel" : 691854321,
        "Pepe" : 676298911,
        "Zeben" : 699812345
        }
    print('1.Mostrar lista de contactos.')
    print('2.Añadir contacto (nombre y teléfono).')
    print('3.Borrar contacto (nombre).')
    print('4.Salir.')
    option = int(input('Elige un número: '))
    if option == 1:
        print(show_contacts(phone_book))
    elif option == 2:
        name = input('Dame un nombre: ')
        phone = int(input('Dame un número de telefono: '))
        print(add_contact(phone_book,name,phone))
    
    elif option == 3:
        name = input('Dame un nombre: ')
        print(remove_contact(phone_book,name))


menu()






        