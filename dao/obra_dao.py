from dao.dao import DAO

#Clase concreta que implementa la interface Data Access Object
class Obra_DAO(DAO):
    def __init__(self) -> None:
        super().__init__()
        self.nombre_tabla = "obras"
    
    @property
    def nombre_tabla(self):
        return self.__nombre_tabla
    
    @nombre_tabla.setter
    def nombre_tabla(self, valor):
        self.__nombre_tabla = valor
    
    def crear_tabla(self):
        try:
            db, cursor = self.conectar_bd()
            # Crear una tabla
            cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.nombre_tabla} (
                "id"	INTEGER,
                "entorno"	TEXT,
                "nombre"	TEXT,
                "descripcion"	TEXT UNIQUE,
                "monto_contrato"	TEXT,
                "direccion"	TEXT,
                "fecha_inicio"	TEXT,
                "fecha_fin_inicial"	TEXT,
                "plazo_meses"	TEXT,
                "porcentaje_avance"	TEXT,
                "licitacion_anio"	TEXT,
                "nro_contratacion"	TEXT,
                "beneficiarios"	TEXT,
                "mano_obra"	TEXT,
                "destacada"	TEXT,
                "expediente_numero"	TEXT,
                "id_etapa"	INTEGER,
                "id_empresa"	INTEGER,
                "id_tipo_obra"	INTEGER,
                "id_area"	INTEGER,
                "id_barrio"	INTEGER,
                "id_tipo_contratacion"	INTEGER,
                "id_fuente_financiamiento"	INTEGER,
                PRIMARY KEY("id" AUTOINCREMENT)
            );''')
        except Exception as e:
            print(f"Ocurrió un error al crear la tabla. {e}")
        finally:
            db.close()
    
    def insertar_registro(self, objeto, lista_id):
        try:
            db, cursor = self.conectar_bd()
            # Insertar un registro a la tabla
            cursor.execute(f'''INSERT INTO {self.nombre_tabla} 
                (entorno,nombre,descripcion,monto_contrato,direccion,fecha_inicio
                ,fecha_fin_inicial,plazo_meses,porcentaje_avance,licitacion_anio
                ,nro_contratacion,beneficiarios,mano_obra,destacada,expediente_numero
                ,id_etapa,id_empresa,id_tipo_obra,id_area,id_barrio,id_tipo_contratacion,id_fuente_financiamiento)
                VALUES
                ('{objeto.entorno}','{objeto.nombre}','{objeto.descripcion}',{objeto.monto_contrato}
                ,'{objeto.direccion}','{objeto.fecha_inicio}','{objeto.fecha_fin_inicial}'
                ,{objeto.plazo_meses},{objeto.porcentaje_avance},{objeto.licitacion_anio}
                ,'{objeto.nro_contratacion}','{objeto.beneficiarios}','{objeto.mano_obra}'
                ,{objeto.destacada},'{objeto.expediente_numero}',{lista_id[0]},{lista_id[1]},{lista_id[2]},{lista_id[3]},{lista_id[4]},{lista_id[5]},{lista_id[6]});'''
            )
            # Guardar (commit) los cambios
            db.commit()
            #print("El registro se ha insertado correctamente")
            return cursor.lastrowid
        except Exception as e:
            #print(f"Ocurrió un error al insertar un registro. {e}")
            return 0
        finally:
            db.close()
    
    def insertar_varios_registros(self, lista):
        for objeto in lista:
            self.insertar_registro(objeto)

    def importar_registro_csv(self, elementos, lista_id):
        try:
            db, cursor = self.conectar_bd()
            # Insertar un registro a la tabla
            cursor.execute(f'''INSERT INTO {self.nombre_tabla}
                (entorno,nombre,descripcion,monto_contrato,direccion,fecha_inicio
                ,fecha_fin_inicial,plazo_meses,porcentaje_avance,licitacion_anio
                ,nro_contratacion,beneficiarios,mano_obra,destacada,expediente_numero
                ,id_etapa,id_empresa,id_tipo_obra,id_area,id_barrio,id_tipo_contratacion,id_fuente_financiamiento)
                VALUES
                ('{elementos[0]}','{elementos[1]}','{elementos[2]}',{elementos[3]}
                ,'{elementos[4]}','{elementos[5]}','{elementos[6]}'
                ,'{elementos[7]}','{elementos[8]}','{elementos[9]}'
                ,'{elementos[10]}','{elementos[11]}','{elementos[12]}'
                ,'{elementos[13]}','{elementos[14]}',{lista_id[0]},{lista_id[1]},{lista_id[2]},{lista_id[3]},{lista_id[4]},{lista_id[5]},{lista_id[6]});'''
            )
            # Guardar (commit) los cambios
            db.commit()
            #print("El registro se ha insertado correctamente")
            return cursor.lastrowid
        except Exception as e:
            #print(f"Ocurrió un error al insertar un registro. {e}")
            return 0
        finally:
            db.close()
    
    def seleccionar_registro(self, objeto):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"SELECT * FROM {self.nombre_tabla} WHERE descripcion='{objeto.descripcion}'")
            print(cursor.fetchone())
        except Exception as e:
            print(f"Ocurrió un error al seleccionar el registro correspondiente a la obra={objeto.descripcion}. {e}")
        finally:
            db.close()
    
    def seleccionar_todos_registros(self):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"SELECT * FROM {self.nombre_tabla}")
            print(cursor.fetchall())
        except Exception as e:
            print(f"Ocurrió un error al seleccionar todos los registros. {e}")
        finally:
            db.close()
    
    def eliminar_registro(self, objeto):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"DELETE FROM {self.nombre_tabla} WHERE descripcion='{objeto.descripcion}'", )
            # Guardar (commit) los cambios
            db.commit()
            print(f"El registro correspondiente a la obra {objeto.descripcion} se ha eliminado correctamente")
        except Exception as e:
            print(f"Ocurrió un error al eliminar el registro correspondiente a la obra {objeto.descripcion}. {e}")
        finally:
            db.close()

    def modificar_registro(self, objeto):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"UPDATE {self.nombre_tabla} SET razon_social='{objeto.razon_social}' WHERE cuit='{objeto.cuit}'", )
            # Guardar (commit) los cambios
            db.commit()
            print(f"Los datos correspondientes a la obra {objeto.descripcion} se ha actualizado correctamente")
        except Exception as e:
            print(f"Ocurrió un error al modificar los datos correspondientes a la obra {objeto.descripcion}. {e}")
        finally:
            db.close()
    
    def obtener_registros(self):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"SELECT * FROM {self.nombre_tabla}")
            return cursor.fetchall()
        except Exception:
            return None
        finally:
            db.close()
    
    def obtener_registro(self, objeto):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"SELECT * FROM {self.nombre_tabla} WHERE descripcion='{objeto.descripcion}'")
            return cursor.fetchone()
        except Exception as e:
            #print(f"Ocurrió un error al seleccionar el registro correspondiente a la obra={objeto.descripcion}. {e}")
            return 0
        finally:
            db.close()
    
    def obtener_registro_desde_csv(self, valor):
        try:
            db, cursor = self.conectar_bd()
            cursor.execute(f"SELECT * FROM {self.nombre_tabla} WHERE descripcion='{valor}'")
            return cursor.fetchone()
        except Exception as e:
            #print(f"Ocurrió un error al seleccionar el registro correspondiente a la descripcion={objeto.descripcion}. {e}")
            return 0
        finally:
            db.close()

