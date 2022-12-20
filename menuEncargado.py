import os
from conexion import Conexion


def menuEncargado():
    os.system('cls')
    print("""====================Menu Encargado=======================
    
        1. 
        2. revisar habitaciones disponibles
        3. 
        4. """)

    opcion = int(input('ingrese una opcion: '))

    while opcion not in [1, 2, 3, 4]:
        print('ingrese una opcion correcta UwU')
    
    if opcion == 1:
        print("CAT")


    if opcion == 2:
        print('=============== revisar habitaciones disponibles ====================')

        conexionDB = Conexion()
        allHabitaciones = conexionDB.mostrarHabitaciones()
        count = 1
        for habitacion in allHabitaciones:
            print("-{} -id: {} -nombre: {}".format(count, habitacion[0], habitacion[1]))
            print("------------------------------------------------------------")
            count += 1
            

