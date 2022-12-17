from conexion import Conexion
from test import cifrar
from login import logIn
import os
os.system('cls')

def menuAdm():
    os.system('cls')
    print("""======================Menu Adminstradror====================

        1. Crear encargado
        2. Buscar encargados
        3. Modificar encargado
        4. Eliminar encaragado
    """)

    opcion = int(input('ingrese una opcion: '))

    while opcion not in [1, 2, 3, 4]:
        print('ingrese una opcion correcta UwU')
    
    if opcion == 1:
        print("====================crear encargaado======================")

        conexionDB = Conexion()

        enc_id = int(input('ingrese el id del encargado: '))
        enc_user = input('ingrese el nombre del encargado: ')
        enc_password = input('ingrese la contraseña del encargado: ')
        
        cifradoPass = cifrar(enc_password)

        conexionDB.insertarEncagados(enc_id,enc_user,cifradoPass)

        print('encargado creado')

    if opcion == 2:
        print("====================Buscar encargaados====================")

        conexionDB = Conexion()
        allEncargados = conexionDB.mostrarEncargados()
        print(allEncargados)

    if opcion == 3:
        print("====================modificar encargaado====================")

        conexionDB = Conexion()
        enc_user = input('ingrese id del encargado a modificar: ')
        enc_newUser = input('ingrese el nuevo nombre del encargado: ')

        conexionDB.updateNameEnc(enc_newUser, enc_user)

    if opcion == 4:
        print("====================eliminar encargaado====================")




#
#
#
#




def menuEncargado():
    os.system('cls')
    print("""====================Menu Encargado=======================""")

























# menu general

def menu():

    print("""
    ===================Menu Principal===================
    Bienvenido al sistema de registro de pasajeros funte de los deseos
    ingrese sus credenciales  
    """)

    entrar =  logIn()

    if entrar:
        if entrar == 'adm':
            menuAdm()
        elif entrar == 'encargado':
            menuEncargado()
    else:
        print('error')

menuAdm()