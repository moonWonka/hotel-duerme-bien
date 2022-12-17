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
        3. Modificar encargado (solo nombre de  momento)
        4. Eliminar encaragado
    """)

    opcion = int(input('ingrese una opcion: '))

    while opcion not in [1, 2, 3, 4]:
        print('ingrese una opcion correcta UwU')
    
    if opcion == 1:
        os.system('cls')
        print("""
            ====================crear encargaado ======================
            
            """)

        conexionDB = Conexion()

        try: 
            enc_id = int(input('ingrese el id del encargado: '))
            enc_user = input('ingrese el nombre del encargado: ')
            enc_password = input('ingrese la contraseña del encargado: ')
            
            cifradoPass = cifrar(enc_password)
            print(cifradoPass)
            conexionDB.insertarEncagados(enc_id,enc_user,cifradoPass)

            print('encargado creado')
        except:
            print('error al crear encargado')

    if opcion == 2:
        os.system('cls')
        print("====================Buscar encargaados====================")

        conexionDB = Conexion()
        allEncargados = conexionDB.mostrarEncargados()
        count = 1
        for encargado in allEncargados:
            print("-{} -id: {} -nombre: {}".format(count, encargado[1], encargado[0]))
            print("------------------------------------------------------------")
            count += 1

    if opcion == 3:
        print("====================modificar encargaado====================")

        conexionDB = Conexion()
        enc_user = input('ingrese id del encargado a modificar: ')
        enc_newUser = input('ingrese el nuevo nombre del encargado: ')

        conexionDB.updateNameEnc(enc_newUser, enc_user)

    if opcion == 4:
        print("====================eliminar encargaado====================")



