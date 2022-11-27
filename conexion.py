import mysql.connector

class Conexion:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host='localhost',
            user = 'root',
            passwd = '',
            database = 'hotel duerme bienk')

        self.cursor = self.conexion.cursor()
        #conectado = self.conexion.is_connected()

        #if conectado:
        #    print('esta conectado')

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
            self.cerrarConexion()
        #select users admins
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
            self.cerrarConexion()

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
            self.cerrarConexion()
 
    # upgrade

    # delete

    def cerrarConexion(self):
        self.cursor.close()
        self.conexion.close()
        print('conexion cerrada! bye')

#-------CRUD tabla Encargado--------------->
    
    def insertarEncagados(self,enc_id,enc_user,enc_password):
        sql="INSERT INTO encargados (enc_id,enc_user,enc_password) VALUE ({}, '{}', '{}')".format(enc_id,enc_user,enc_password)
        try:
            self.cursor.execute(sql)
            self.connection.commit()    
            print("cuenta ingresada")
        except Exception as e:
            raise e

    def mostrarEncargados(self):
        sql="SELECT enc_user FROM encargados"
        try:
            self.cursor.execute(sql)
            query = self.cursor.fetchall()
            return query
        except Exception as err:
            print('error al realizar la consulta', err)
        finally:
            self.cursor.close()
    
    def mostrarPassEnc(self,enc_user):
        sql = "SELECT enc_password FROM encargados WHERE enc_user = '{}'".format(enc_user)
        try:
            self.cursor.execute(sql)
            query = self.cursor.fetchone()
            return query[0]
        except Exception as err:
            print('error al realizar la consulta pass', err)
        finally:
            self.cursor.close()
    
    def updatePassEnc(self,enc_user,enc_password):
        sql= "UPDATE encargados SET enc_password='{}' WHERE enc_user='{}'".format(enc_password,enc_user)
        #print(sql)
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
        except Exception as e:
            raise e
    
    def updateNameEnc(self,enc_user,new):
        sql= "UPDATE encargados SET enc_user='{}' WHERE enc_user='{}'".format(new,enc_user)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
        except Exception as e:
            raise e

    def deleteEnc(self,enc_user):
        sql="DELETE FROM encargados WHERE enc_user = '{}'".format(enc_user)
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
        except Exception as e:
            raise e