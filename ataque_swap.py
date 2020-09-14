import sqlite3
from sqlite3 import Error
import binascii, os

db_file = 'storage.db'

def conection(db_file):
    cnn = None
    try: 
        cnn = sqlite3.connect(db_file)
        return cnn

    except Error as e:
        print (e)
    return cnn

def actualizar_claves():       
    try:
        #coneccion a la db, la crea si no existe
        cnn = conection(db_file)
        c = cnn.cursor()
        
        # c.execute("""CREATE TABLE tmpinfoswap (name text,password text);""")

        c.execute("SELECT name, password FROM info ORDER BY name DESC LIMIT 1;")
        rows=c.fetchall()
        if len(rows) == 0:
            cnn.close()
            return None
        else:
            for row in rows: 
                name = row[0]
                site_pass = row[1]

        # c.execute("INSERT INTO tmpinfoswap(name, password) VALUES(?,?)", (name, site_pass,))        

        c.execute("SELECT name, password FROM info ORDER BY name ASC LIMIT 1;")
        rows=c.fetchall()
        if len(rows) == 0:
            cnn.close()
            return None
        else:
            for row in rows: 
                name_n = row[0]
                site_pass_n = row[1]
            
        # c.execute("INSERT INTO tmpinfoswap(name, password) VALUES(?,?)", (name_n, site_pass_n,))        

        c.execute("UPDATE info SET password =? WHERE name=?", (site_pass_n, name,))

        c.execute("UPDATE info SET password =? WHERE name=?", (site_pass, name_n,))

        # c.execute("DROP TABLE tmpinfoswap")

        cnn.commit()

        cnn.close()

    except Error as e: 
        print(e)


actualizar_claves()