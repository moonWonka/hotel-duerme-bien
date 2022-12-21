from login import logIn
from menuAdmin import menuAdm
from menuEncargado import menuEncargado
import os
os.system('cls')

# menu general

def menu():

    while True:
        print("""
        ===================Menu Principal===================
        Bienvenido al sistema de registro de pasajeros funte de los deseos 
        
        
        
        
        Para Ingresar presiona 1 y Enter
        Para salir presiona 9 y Enter
        """)
        opt=int(input("Ingresa Opcion: "))
        if opt==1:
            os.system("cls")
            print("Ingrese sus credenciales: ")
            entrar =  logIn()

            if entrar:
                if entrar == 'adm':
                    menuAdm()
                elif entrar == 'encargado':
                    menuEncargado()
            else:
                print('error')
        
        if opt==9:
            os.system("cls")
            input("Adios")
        
            break

        else:
            print("Ingresa una opcion valida")
