from login import logIn
from menuAdmin import menuAdm
import os
os.system('cls')

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

