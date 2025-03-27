import sqlite3
#crar variables ce conexion 
conn = sqlite3.connect("Base_de_datos_db")
curso = conn.cursor()# el cursos de base de dato 
#crear tabla 
curso.execute(
    """CREATE TABLE IF NOT EXISTS comentario(
        id_comentario  INTEGRE PRIMARY KEY ,
        tipo_de_comentariO TEXT NOT NULL,
        fecha TEXT NOT NULL
    )
    """
)
conn.commit()
curso.execute("INSERT INTO comentario (tipo_de_comentariO,fecha)VALUES(?,?)",
              ("comentrio","2019,10,29"))
conn.commit()

curso.execute("SELECT * FROM comentario")
comentario = curso.fetchall()
for comentarios in comentario:
        print(comentarios)
#curso.execute("DELETE FROM  comentario")
#conn.commit()        