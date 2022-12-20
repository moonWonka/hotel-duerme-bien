import os
from conexion import Conexion


def menuEncargado():
    os.system('cls')
    print("""====================Menu Encargado=======================
    
        1. Registro Pasajeros
        2. revisar habitaciones disponibles
        3. cambiar estado de habitacion
        4. """)

    opcion = int(input('ingrese una opcion: '))

    while opcion not in [1, 2, 3, 4]:
        print('ingrese una opcion correcta UwU')
    
    if opcion == 1:
        os.system('cls')
        print("Registro Pasajeros")
        print("ingrese los datos del pasajero")
        cli_nombre = input("ingrese el nombre del pasajero: ")
        cli_apellidoP = input("ingrese el apellido del pasajero: ")
        cli_apellidoM = input("ingrese el apellido del pasajero: ")
        cli_rut = input("ingrese el rut del pasajero: ")



    if opcion == 2:
        os.system('cls')
        print('=============== revisar habitaciones disponibles ====================')

        conexionDB = Conexion()
        allHabitaciones = conexionDB.mostrarHabitaciones()
        for habitacion in allHabitaciones:

            print("habitacion n°: {}".format(habitacion[1]))
            print("tipo: {}".format(habitacion[4]))
            print("ubicacion: {}".format(habitacion[2]))
            print("costo: {}".format(habitacion[5]))
            print("capacidad: {}".format(habitacion[4]))
            print("------------------------------------------------------------")
    
    if opcion == 3:
        os.system('cls')
        print('=============== cambiar estado de habitacion ====================')
        
        numeroHabitacion = input('ingrese el numero de la habitacion: ')
        estadoHabitacion = input('ingrese el nuevo estado de la habitacion: ')
        
        try:
            conexionDB = Conexion()
            conexionDB.modificarEstadoHabitacion(numeroHabitacion, int(estadoHabitacion))
            print('estado de habitacion modificado')
        except:
            print('error al modificar estado de habitacion')
        

    if opcion == 4:
        os.system('cls')
        pass


menuEncargado()