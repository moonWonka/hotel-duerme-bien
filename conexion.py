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

#-------CRUD tabla Administradores--------------->

    def mostrarUsersAdmin(self):
        sql = 'select adm_user from administradores'
        try:
            self.cursor.execute(sql)
            query = self.cursor.fetchall()
            #print(query)
            return query
        except Exception as err:
            print('error al realizar la consulta', err)
        finally:
            self.cursor.close()

    def mostrarUserPass(self, user):
        sql = "select adm_pass from administradores where adm_user = '{}'".format(user)
        try:
            self.cursor.execute(sql)
            query = self.cursor.fetchone()
            #print(query[0])
            return query[0]
        except Exception as err:
            print('error al realizar la consulta pass', err)
        finally:
            self.cursor.close()

    # insertar
    def insertarUserAdmin(self):
        #INSERT INTO administradores (adm_id, adm_user, pass) VALUES (111, 'willy', 123); 
        sql = "INSERT INTO administradores VALUES (22, 'dany', 123)"
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
        except Exception as err:
            print('error al realizar el insert', err)
        finally:
            self.cursor.close()


    # upgrade

    # delete

    def cerrarConexion(self):
        self.conexion.close()
        print('conexion cerrada! bye')

#a = Conexion()
#a.mostrarUserPass('willy')
# a.mostrarUsersAdmin()
# a.insertarUserAdmin()
# a.mostrarUsersAdmin()



#guardado ejemplo