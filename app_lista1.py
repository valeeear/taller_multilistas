list_id = []
list_name = []
list_contact = []
list_e_mail = []
import os

def fnt_limpiar():
    os.system('cls')
    print('Autor: Valentina Arias')
    print('Fecha: 18 de abril del 2024\n\n')
    
def fnt_registrar(id, name, contact, e_mail):
    if id == '' or name == '' or contact == '' or e_mail == '':
        enter = input('Error, debe ingresar todos los datos <ENTER>')
    else:
            list_id.append(id)
            list_name.append(name)
            list_contact.append(contact)
            list_e_mail.append(e_mail)
            enter = input(f'\nLa persona ha sido registrada con éxito <ENTER>')  
    
def fnt_selector(opcion):
    fnt_limpiar()
    if opcion == '1':
        id = input('ID:     ')
        if id in list_id:
            enter = input('\nEsta persona ya se encuentra registrada <ENTER>')
        else:
            name = input('NOMBRE: ')
            contact = input('CONTACTO: ')
            e_mail = input('EMAIL: ')
            fnt_registrar(id, name, contact, e_mail)
    elif opcion == '2':
        fnt_limpiar()
        for i in range(len(list_id)):
            print(f'{list_id[i]}     {list_name[i]}     {list_contact[i]}     {list_e_mail[i]}')
        enter = input('\nPresione ENTER para continuar...')
            
                      
sw= True
while sw == True:
    fnt_limpiar()
    op = input('\n\n>>>>>>MENÚ PRINCIPAL<<<<<<<\n1. Registrar\n2. consultar\n3. salir\n->')
    fnt_selector(op)

        
        
        
    
