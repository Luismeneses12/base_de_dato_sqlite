import sqlite3

#crae variables de conexion 

conexion = sqlite3.connect("Base_de_datos.db")#agregar ina base d edatos como existente 
curso_db = conexion.cursor()#crear n cursos de la base de datos 
#crar tabla de base de dato si no existe 



curso_db.execute(
    """CREATE TABLE IF NOT EXISTS admin(       
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad  INTEGER,
    correo TEXT UNIQUE
    )
    """
) 
conexion.commit()
#insetar  un solo registro  en la tabla 
curso_db.execute("INSERT INTO usuario (nombre,edad,correo)VALUES(?,?,?)",
                 ("luisa",29,"cal@email.com")
                 )
conexion.commit()
#insertar  multiples registro 
usuario_nuevos = [("juana",29,"lj@email.com"),("jefersonr",30,"jn@email.com")]
#insertar varios usuario 
curso_db.executemany("INSERT INTO usuario (nombre,edad,correo)VALUES(?,?,?)",
                    usuario_nuevos)
conexion.commit()
#consultar  los datos en la tabla 
curso_db.execute("SELECT * FROM usuario")
usuario = curso_db.fetchall()#obtener todos los registro 
#mostrar todos los resultados 
for usuarios in usuario:
    print(usuarios)
#actializar datos 
curso_db.execute("UPDATE usuario SET edad = ? WHERE nombre = ?",
                 (35,"juan"))
conexion.commit()
#eliminar un dato especifico 
curso_db.execute("DELETE FORM usuario   WHERE nombre=?",
                 ("jenifer",))
conexion.commit()
#para eliminar todos los registros 
curso_db.execute("DELETE FROM usuario")
conexion.commit()

#cerrar la conexion
conexion.close()    

