import os
from conexion import Conexion


def menuEncargado():
    
    while True:

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
            conexionDB = Conexion()
            os.system('cls')
            print("===========Ingrese los datos del Cliente==============")
            cli_nombre = input("Ingrese el nombre del Cliente: ")
            cli_apellidoP = input("Ingrese el apellido paterno del Cliente: ")
            cli_apellidoM = input("Ingrese el apellido materno del Cliente: ")
            cli_rut = input("Ingrese el rut del Cliente: ")
            conexionDB.ingresarCli(cli_rut, cli_nombre,cli_apellidoP, cli_apellidoM) 
            input()



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
            input()
        
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
            input()
            

        if opcion == 4:
            os.system('cls')
            input("Cerraste sesión")
            break
        

