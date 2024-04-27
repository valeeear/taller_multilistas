list_nombre_completo = []
list_correo = []
list_identificacion = []
list_contacto = []
list_edad = []
list_años_experiencia = []
list_profesion = []
list_ciudad = []
list_sexo = []
import os

def fnt_limpiar():
    os.system('cls')
    print('AUTOR: Valentina Arias Raigosa ')
    print('FECHA: 18 de abril 2024')

def fnt_registrar_candidatos(nombres, correo, identificacion, contacto, edad, años_experiencia, profesion, ciudad, sexo):
    if nombres == ' ' or correo == ' ' or identificacion == ' ' or contacto == ' ' or edad == ' ' or años_experiencia == ' ' or profesion == ' ' or ciudad == ' ' or sexo == ' ':
        print('Llene todos los campos')
    elif (24 <= edad <= 35) and (2 <= años_experiencia <= 4) and (profesion == '1' or profesion == '2') :
        list_nombre_completo.append(nombres)
        list_correo.append(correo)
        list_identificacion.append(identificacion)
        list_contacto.append(contacto)
        list_edad.append(edad)
        list_años_experiencia.append(años_experiencia)
        list_profesion.append(profesion)
        list_ciudad.append(ciudad)
        list_sexo.append(sexo)
        enter = input('\n Has sido registrado a la lista para la selección de empleados\nPresiones <ENTER> para continuar')
    else:
        enter = input('Las condiciones no se cumplen\nPresione <ENTER> para continuar')

def fnt_consultar_candidatos():
    fnt_limpiar()
    print('\n<<< LISTA DE CANDIDATOS >>>\n')
    for i in range(len(list_identificacion)):
        print(f'Nombre: {list_nombre_completo[i]}')
        print(f'Correo: {list_correo[i]}')
        print(f'Identificación: {list_identificacion[i]}')
        print(f'Contacto:{list_contacto[i]}')
        print(f'Edad: {list_edad[i]}')
        print(f'Años de experiencia: {list_años_experiencia[i]} años')
        print(f'Profesion: {list_profesion[i]}')
        print(f'{list_profesion[i]}') 
        print(f'Ciudad:{list_ciudad[i]}')
        print(f'Sexo: {list_sexo[i]}')
        
def fnt_selector(op):
    fnt_limpiar()
    if op == '1':
            nombres = input('\nNOMBRE COMPLETO:  ')
            identificacion = input('\nIDENTIFICACIÓN:  ')
            correo = input('\nCORREO:  ')
            contacto = input('\nCONTACTO:  ')
            edad = int(input('\nEDAD: '))
            años_experiencia = int(input('\nAÑOS DE EXPERIENCIA:  '))
            profesion = input('\nPROFESIÓN\n1. Ing. Sistemas\n2. Ing. Informatica\n3. Otra--> ')
            ciudad = input('\nCIUDAD:  ')
            sexo = input('\nSEXO:  ')
            fnt_registrar_candidatos(nombres, correo, identificacion, contacto, edad, años_experiencia, profesion, ciudad, sexo)
    elif op == '2':
        fnt_consultar_candidatos()
        enter = input('\nPresiona <ENTER> para continuar...')
    elif op == '3':
        sw = False

sw = True
while sw == True:
    fnt_limpiar()
    op = input('\n<<<<MENÚ PRINCIPAL>>>> \n1. REGISTRAR CANDIDATOS \n2. LISTA DE SELECCIONADOS \n3. SALIR \n-> ')
    fnt_selector(op)
  
