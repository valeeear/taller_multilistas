list_nombrecompleto = []
list_identificacion = []
list_correo = []
list_edad = []
list_exper = []
list_profesion = []
list_ciudad = []
list_sexo = []
import os

def fnt_limpiar():
    os.system('cls')
    print('Autor: Valentina Arias')
    print('Fecha: 2024-19-03')

def fnt_registrar(nombre, identificacion, correo, edad, experiencia, profesion, ciudad, sexo):
    if nombre == '' or identificacion == '' or correo == '' or edad == '' or experiencia == '' or profesion == '' or ciudad == '' or sexo == '':
        print('Llene todos los campos')
    else:
        list_nombrecompleto.append(nombre)
        list_identificacion.append(identificacion)
        list_correo.append(correo)
        list_edad.append(edad)
        list_exper.append(experiencia)
        list_profesion.append(profesion)
        list_ciudad.append(ciudad)
        list_sexo.append(sexo)
        fnt_limpiar()
        print('Registro exitoso')
        
def fnt_selector(opcion):
    fnt_limpiar()
    if opcion == '1':
        nombre =input('NOMBRE:   ')
        identificacion = input('IDENTIFICACION:   ')
        correo = input('CORREO:   ')
        edad = input('EDAD:   ')
        experiencia = input('EXPERIENCIA:   ')
        profesion = input('PROFESION\n1. Ing. Sistemas\n2. Ing. Informatica:\n3. Otro\n4.->  ')
        ciudad = input('CIUDAD:   ')
        sexo = input('SEXO:   ')
        if edad >= '25' or edad <='35' and profesion == 'Ing. sistemas' or profesion== 'Ing. informatica' and experiencia >= '2' or experiencia <='4':
            print('{nombre} has sido regisrado en la lista para la seleccion de empleados')
            fnt_registrar(nombre, identificacion, correo, edad,experiencia, profesion, ciudad, sexo)
            
        else:
            enter =('No cumples con los requisitos >ENTER<')
    elif opcion == '2':
        fnt_limpiar()
        for i in range(len(list_nombrecompleto)):
            print(f'{list_nombrecompleto[i]}     {list_identificacion[i]}     {list_correo[i]}    {list_edad[i]}    {list_exper[i]}    {list_profesion[i]}    {list_ciudad[i]}    {list_sexo[i]}')
        enter = input('\nPresione ENTER para continuar...')
    elif opcion == '3':
        sw = False
        
sw = True
while sw == True:
    fnt_limpiar()
    op = input('\n\n>>>>>MENÚ PRINCIPAL<<<<<\n1. Registrar\n2. Consultar\n3. Salir\n->')
    fnt_selector(op)