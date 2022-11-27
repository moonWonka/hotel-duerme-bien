from login import logIn
import os
os.system('cls')
def menu():

    print("""
    Bienvenido al sistema de registro de pasajeros funte de los deseos
    ingrese sus credenciales  
    """)

    entrar =  logIn()

    if entrar:
        print('wolo')
    else:
        print('error')

    


menu()