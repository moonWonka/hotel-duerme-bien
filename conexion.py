import mysql.connector

class Conexion:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host='20.226.74.184',
            user = 'wonka',
            passwd = '',
            database = 'hotelk')

        self.cursor = self.conexion.cursor()
        #conectado = self.conexion.is_connected()

        #if conectado:
        #    print('esta conectado')

#-------CRUD tabla Administradores--------------->
#--------------selects--------------->

    def mostrarUsersAdmin(self):
        sql = 'select adm_user from administradores'
        try:
            self.cursor.execute(sql)
            query = self.cursor.fetchall()
            return query
        except Exception as err:
            print('error al realizar la consulta', err)
        finally:
            self.cerrarConexion()

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
#------------------------------------------------------->
    # insertar
    def insertarUserAdmin(self):
        #INSERT INTO administradores (adm_id, adm_user, pass) VALUES (111, 'willy', 123); 
        sql = "INSERT INTO administradores VALUES (22, 'dany', 123)"
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
        except Exception as err:
            print('error al realizar el insert', err)
 
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
            self.conexion.commit()    
            print("Cuenta ingresada")
        except Exception as err:
            print('ERROR: No se realizo la operación', err)
        finally:
            self.cerrarConexion()

    def mostrarEncargados(self):
        sql="SELECT enc_user FROM encargados"
        try:
            self.cursor.execute(sql)
            query = self.cursor.fetchall()
            return query
        except Exception as err:
            print('ERROR: problemas al realizar la consulta', err)
        finally:
            self.cerrarConexion()
    
    def mostrarPassEnc(self,enc_user):
        sql = "SELECT enc_password FROM encargados WHERE enc_user = '{}'".format(enc_user)
        try:
            self.cursor.execute(sql)
            query = self.cursor.fetchone()
            return query[0]
        except Exception as err:
            print('ERROR: problemas al realizar la consulta', err)
        finally:
            self.cerrarConexion()
    
    def updatePassEnc(self,enc_user,enc_password):
        sql= "UPDATE encargados SET enc_password='{}' WHERE enc_user='{}'".format(enc_password,enc_user)
        #print(sql)
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
        except Exception as err:
            print('ERROR: No se realizo la operación', err)
        finally:
            self.cerrarConexion()
    
    def updateNameEnc(self,enc_user,new):
        sql= "UPDATE encargados SET enc_user='{}' WHERE enc_user='{}'".format(new,enc_user)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
        except Exception as err:
            print('ERROR: No se realizo la operación', err)
        finally:
            self.cerrarConexion()

    def deleteEnc(self,enc_user):
        sql="DELETE FROM encargados WHERE enc_user = '{}'".format(enc_user)
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
        except Exception as err:
            print('ERROR: No se realizo la operación', err)
        finally:
            self.cerrarConexion()

#-------CRUD Hab--------------->

    def mostrarHabitaciones(self):
        sql="SELECT hab_id,hab_numero_hab,hab_ubicacion,hab_capacidad,hab_tipo,hab_costo FROM habitaciones where hab_estado=1"
        #0 False - 1 True
        try:
            self.cursor.execute(sql)
            lista = self.cursor.fetchall()
            print(lista)
            return lista
        except Exception as err:
            print('ERROR: problemas al realizar la consulta', err)
        finally:
            self.cerrarConexion()
    
    def ingresarHab(self,hab_id,hab_numero_hab,hab_ubicacion,hab_capacidad,hab_tipo,hab_costo):
        sql="INSERT INTO habitaciones (hab_id,hab_numero_hab,hab_ubicacion,hab_capacidad,hab_tipo,hab_costo,hab_estado) VALUES ({},'{}','{}',{},'{}',{},1)".format(hab_id,hab_numero_hab,hab_ubicacion,hab_capacidad,hab_tipo,hab_costo)

        try:
            self.cursor.execute(sql)
            self.conexion.commit()    
            print("La habitación fue correctamente ingresada")
        except Exception as err:
            print('ERROR: No se realizo la operación', err)
        finally:
            self.cerrarConexion()
    
    def borrarHab(self,hab_numero_hab):
        sql="UPDATE habitaciones SET hab_estado = '0' WHERE habitaciones.hab_numero_hab = '{}'".format(hab_numero_hab)
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
            print("Habitación eliminada")
        except Exception as err:
            print('ERROR: No se realizo la operación', err)
        finally:
            self.cerrarConexion()

    def borrarHabDefinitiva(self,hab_numero_hab):
        sql="DELETE FROM habitaciones WHERE hab_numero_hab= '{}'".format(hab_numero_hab)
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
            print("La Habitacion se ha eliminado para siemore")
        except Exception as err:
            print('ERROR: No se realizo la operación', err)
        finally:
            self.cerrarConexion()

#-------CRUD Clientes--------------->

    def ingresarCli(self,cli_id, cli_rut, cli_nombre,cli_apellidoP, cli_apellidoM):
        sql="INSERT INTO clientes(cli_id, cli_rut, cli_nombre,cli_apellidoP, cli_apellidoM) VALUES ({},'{}','{}','{}','{}')".format(cli_id, cli_rut, cli_nombre,cli_apellidoP, cli_apellidoM)
        try:
            self.cursor.execute(sql)
            self.conexion.commit()    
            print("El cliente se a ingresado")
        except Exception as err:
            print("ERROR: No se realizo la operación", err)
        finally:
            self.cerrarConexion()

    def modidficarCli(self,cli_id, cli_rut, cli_nombre,cli_apellidoP, cli_apellidoM):
        sql="UPDATE clientes SET cli_id={},cli_rut='{}',cli_nombre='{}',cli_apellidoP='{}',cli_apellidoM='{}' WHERE cli_id={}".format(cli_id, cli_rut, cli_nombre,cli_apellidoP, cli_apellidoM,cli_id)
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
            print("Datos actualizados")
        except Exception as err:
            print("ERROR: No se realizo la operación", err)
        finally:
            self.cerrarConexion()

#-------CRUD Clientes--------------->

    def ingresarHue(self,id_hue, cli_id, det_id):
        sql="INSERT INTO huespedes(id_hue, cli_id, det_id) VALUES ({},{},{})".format(id_hue, cli_id, det_id)
        try:
            self.cursor.execute(sql)
            self.conexion.commit()    
            print("El Huésped se a ingresado")
        except Exception as err:
            print("ERROR: No se realizo la operación", err)
        finally:
            self.cerrarConexion()
    
    def eliminarHue(self,id_hue):
        sql="DELETE FROM huespedes WHERE id_hue={}".forma(id_hue)

#-------CRUD Clientes--------------->


#asd=Conexion()
#asd.borrarHabDefinitiva("330a")
#asd.ingresarHab(3,"230","Tercer Piso",1,"Individual",20000)
