from conexion import Conexion

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

def buscarUserPass(user):
#------------si es un admin---------->
    encontradoAdm = buscarUserAdmin(user)

    if encontradoAdm:
        return 'adm'

#------------si es un admin---------->
    encontradoEncargado = buscarUserEncargado(user)

    if encontradoEncargado:
        return 'encargado' 
    else:
#------------si no se encuntra----------> 
        return False

def buscarPassEncargado(user, userPass):
    conectar = Conexion()
    passGuardada = conectar.mostrarPassEnc(user)
    if passGuardada == str(userPass):
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

def logIn():

    #pedir credenciales
    userName = input('ingrese su usuario: ')
    userPass = int(input('ingrese su password: '))

    #buscar un suario en base de datos
    encontrado = buscarUserAdmin(userName)

    if encontrado == 'adm':
        credenciales = buscarPassAdm(userName, userPass)
        if credenciales:
            return 'adm'          
    elif encontrado == 'encargado':
        credenciales = buscarPassEncargado(userName, userPass) 
        if credenciales:
            return 'encargado'
    else:
        return False

