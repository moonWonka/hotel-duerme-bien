import os
from conexion import Conexion


def menuEncargado():
    
    while True:

        os.system('cls')
        print("""====================Menu Encargado=======================
        
            1. Registro Pasajeros
            2. Revisar Habitaciones Disponibles (para ser ocupadas por pasajeros)
            3. Cambiar Estado de Habitacion
            4. Crear Habitacion
            5. Modificar Habitacion
            9. Salir
            """)

        opcion = int(input('ingrese una opcion: '))

        while opcion not in [1, 2, 3, 4, 9]:
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
            print('=============== crear habitacion ====================')
            
            numeroHabitacion = input('ingrese el numero de la habitacion: ')
            ubicacionHabitacion = input('ingrese la ubicacion de la habitacion: ')
            tipoHabitacion = input('ingrese el tipo de habitacion: ')
            capacidadHabitacion = input('ingrese la capacidad de la habitacion: ')
            costoHabitacion = input('ingrese el costo de la habitacion: ')
            
            try:
                conexionDB = Conexion()
                conexionDB.crearHabitacion(numeroHabitacion, ubicacionHabitacion, tipoHabitacion, int(capacidadHabitacion), int(costoHabitacion))
                print('habitacion creada')
            except:
                print('error al crear habitacion')
            input()

        if opcion == 5:
            os.system('cls')
            print('=============== modificar habitacion ====================')
            
            numeroHabitacion = input('ingrese el numero de la habitacion: ')
            costoHabitacion = input('ingrese el costo de la habitacion: ')
            try:
                conexionDB = Conexion()
                conexionDB.modificarHabitacion(numeroHabitacion, int(costoHabitacion))
                print('habitacion modificada')
            except:
                print('error al modificar habitacion')
            input()

        if opcion == 9:
            os.system('cls')
            input("Cerraste sesión")
            break
        

