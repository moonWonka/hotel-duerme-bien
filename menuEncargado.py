import os
from conexion import Conexion


def menuEncargado():
    os.system('cls')
    print("""====================Menu Encargado=======================
    
        1. 
        2. 
        3. 
        4. """)

    opcion = int(input('ingrese una opcion: '))

    while opcion not in [1, 2, 3, 4]:
        print('ingrese una opcion correcta UwU')
    
    if opcion == 1:
        print("CAT")
