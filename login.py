from conexion import Conexion

def buscarUser(user):
    conectar = Conexion()
    users = conectar.mostrarUsersAdmin()
    conectar.cerrarConexion()
    usersList = []

    for usuario in users:
        usersList.append(usuario[0])

    if user in usersList:
        print('user encotrado')
        return True
    else:
        return False

def buscarPass(user, userPass):
    conectar = Conexion()
    passGuardada = conectar.mostrarUserPass(user)
    conectar.cerrarConexion()
    #print(type(passGuardada), 'wonka', type(userPass))
    if passGuardada == userPass:
        print('Bienvenido')
        return True
    else:
        False

def logIn():

    #pedir credenciales
    userName = input('ingrese su usuario: ')
    userPass = int(input('ingrese su password: '))

    #buscar usuario en base de datos
    encontrado = buscarUser(userName)

    if encontrado:
        #revisar password en base de datos
        verificarPass = buscarPass(userName, userPass)

        if verificarPass:
            return True
        else:
            print('credenciales incorrectas')
            return False
    else:
        print('credenciales incorrectas')
        return False

