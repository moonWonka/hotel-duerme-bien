from conexion import Conexion
from test import cifrar

def buscarUserAdmin(user):
    consultaDB = Conexion()
    consultaAdmin = consultaDB.mostrarUsersAdmin()
    #print(consultaAdmin)
    usersList = []
    
    for usuario in consultaAdmin:
        usersList.append(usuario[0])

    if user in usersList:
        return True
    else:
        return False

def buscarUserEncargado(user):
    consultaDb = Conexion()
    consultaEncargados = consultaDb.mostrarEncargados()
    #print(consultaEncargados)
    usersList = []

    for usuario in consultaEncargados:
        usersList.append(usuario[0])

    if user in usersList:
        return True
    else:
        return False

def buscarTipoUser(user):
#------------si es un admin---------->
    encontradoAdm = buscarUserAdmin(user)

    if encontradoAdm:
        print('Bienvenido administrador')
        return 'adm'

#------------si es un encargado---------->
    encontradoEncargado = buscarUserEncargado(user)

    if encontradoEncargado:
        print('Bienvenido encargado')
        return 'encargado' 
    else:
#------------si no se encuntra----------> 
        return False

def buscarPassEncargado(user, userPass):
    conectar = Conexion()
    passGuardada = conectar.mostrarPassEnc(user)
    if passGuardada == userPass:
        return True
    else:
        print('Error en contraseña')
        return False
    
def buscarPassAdm(user, userPass):
    conectar = Conexion()
    passGuardada = conectar.mostrarUserPass(user)
    #print(type(passGuardada), 'wonka', type(userPass))
    if passGuardada == userPass:
        return True
    else:
        print('Error en contraseña')
        return False

#funcion principal
def logIn():

    #pedir credenciales
    userName = input('ingrese su usuario: ')
    userPass = input('ingrese su password: ')

    userPassCifrada = cifrar(userPass)

    #buscar un suario en base de datos
    encontrado = buscarTipoUser(userName)

    if encontrado == 'adm':
        credenciales = buscarPassAdm(userName, userPassCifrada)
        if credenciales:
            return 'adm'          
    elif encontrado == 'encargado':
        credenciales = buscarPassEncargado(userName, userPassCifrada) 
        if credenciales:
            return 'encargado'
    else:
        return False

