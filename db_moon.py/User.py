# se import la libreria 
import sqlite3
# se crea la variable para la coneccion 
conn = sqlite3.connect("MOON")
#sea crea la ejecucion para la claves foranias 
conn.execute("PRAGMA FOREIN_KEY = ON ")
#se crea el curso para la sabe de datos 
curso = conn.cursor()
# se procede a crear tablas de usuario 
curso.execute("""CREATE TABLE  IF NOT EXISTS uusario (
    ID_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE TEXT ,
    APELLIDO TEXT,
    TELEFONO TEXT,
    CORREO_ELETRONICO TEXTO ,
    FECHA_DE_CREACION  TEXT DEFAULT DATETIME('now',"locatime")
) 
              """              
              )
conn.commit