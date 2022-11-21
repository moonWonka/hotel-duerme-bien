import mysql.connector

class Conexion:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host='localhost',
            user = 'root',
            passwd = '',
            database = 'hotel duerme bienk')

        self.cursor = self.conexion.cursor()
        conectado = self.conexion.is_connected()

        if conectado:
            print('esta conectado')
        else:
            print('error al conectar a la base de datos')
        

    def mostrarUsersAdmin(self):
        sql = 'select adm_user from administradores'
        try:
            self.cursor.execute(sql)
            query = self.cursor.fetchall()
            print(query)
            return query
        except Exception as err:
            print('error al realizar la consulta', err)


    # insertar
    def insertarUserAdmin(self):
        #INSERT INTO administradores (adm_id, adm_user, pass) VALUES (111, 'willy', 123); 
        sql = "INSERT INTO administradores VALUES (22, 'dany', 123)"
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
        except Exception as err:
            print('error al realizar la consulta', err)

    # upgrade

    # delete

a = Conexion()
a.mostrarUsersAdmin()
a.insertarUserAdmin()
a.mostrarUsersAdmin()