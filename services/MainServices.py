#-----------------------------------------------------#
import sqlite3
#-----------------------------------------------------#
from models.user_model import InsertUserModel
from models.user_model import UserCiModel
#-----------------------------------------------------#
class MainServices:
    #-----------------------------------------------------#
    def __init__(self) -> None:
        self.conexion = sqlite3.connect('data/bd_crud.db')
        self.cur = self.conexion.cursor()
        
        try:
            self.cur.execute("""create table Users (
                                    id integer primary key autoincrement,
                                    nombre text,
                                    apellido text,
                                    direccion text,
                                    ci interger,
                                    estado_civil text,
                                    fecha_nac text
                                )""")
            print("se creo la tabla Users")                        
        except sqlite3.OperationalError:
            print("La tabla Users ya existe")                    
    #-----------------------------------------------------#
    def InsertUser(self, usuario: InsertUserModel):
            ci_us_exist=self.cur.execute("SELECT * FROM Users WHERE ci = ?", (usuario.ci,))
            if ci_us_exist.fetchone():
                print(ci_us_exist.fetchone())
                return "Ya el Usuario existe en la base de datos"
            else:
                try:
                    self.cur.execute(
                        "INSERT INTO Users (nombre, apellido, direccion, ci, estado_civil, fecha_nac) VALUES (?, ?, ?, ?, ?, ?)",
                        (usuario.nombre, usuario.apellido, usuario.direccion, int(usuario.ci), usuario.estado_civil, usuario.fecha_nac)
                    )
                    self.conexion.commit()
                    return 'Usuario ingresado correctamente'
                except sqlite3.Error as e:
                    return f"Error al insertar datos en la base de datos: {str(e)}"
                finally:
                    self.cur.close()
    #-----------------------------------------------------#     
    def SearchUser(self, ci: UserCiModel):
        self.cur.execute("SELECT * FROM Users WHERE ci = ?", (ci.ci,))
        result = self.cur.fetchall()
        return result
    #-----------------------------------------------------#
    def DeleteUser(self, user_id):
        try:
            # Borra el usuario por su ID
            self.cur.execute("DELETE FROM Users WHERE id = ?", (user_id,))
            self.conexion.commit()
            return(f'Usuario con ID {user_id} eliminado correctamente')
        except sqlite3.Error as e:
            return(f"Error al eliminar el usuario de la base de datos: {str(e)}")
        finally:
            self.cur.close()
    #-----------------------------------------------------#
    def UpdateUser(self,user_id, usuario: InsertUserModel):
        try:
            self.cur.execute("""
                UPDATE Users
                SET nombre = ?, apellido = ?, direccion = ?, estado_civil = ?, fecha_nac = ?
                WHERE id = ?
            """, (usuario.nombre, usuario.apellido, usuario.direccion, usuario.estado_civil, usuario.fecha_nac,user_id))
            self.conexion.commit()
            return('Datos actualizados correctamente')
        except sqlite3.Error as e:
            return(f"Error al actualizar datos en la base de datos: {str(e)}")
        finally:
            self.cur.close()
    #-----------------------------------------------------#