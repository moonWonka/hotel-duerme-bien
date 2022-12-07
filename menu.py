from login import logIn
import os
os.system('cls')

def menuAdm():
    os.system('cls')
    print("""======================Menu Adminstradror====================0
        1. Crear encargado
        2. Mostar encargados
        3. Modificar encargado
        4. Eliminar encaragado
    """)

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

menu()