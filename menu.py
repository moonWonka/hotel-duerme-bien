from login import logIn
import os
os.system('cls')

def menuAdm():
    #os.system('cls')
    print("""Menu Adminstradror""")

def menuEncargado():
    os.system('cls')
    print("""Menu Encargado""")

def menu():

    print("""
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