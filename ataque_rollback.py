import sqlite3
from sqlite3 import Error
import binascii, os
from cifrado import *

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
        
        c.execute("""CREATE TABLE IF NOT EXISTS tmpinfo (name text,password text, nonce text, tag text);""")

        c.execute("SELECT name, password, nonce, tag FROM info LIMIT 1")
        rows=c.fetchall()
        if len(rows) == 0:
            cnn.close()
            return None
        else:
            for row in rows: 
                name = row[0]
                site_pass = row[1]
                site_nonce = row[2]
                site_tag = row[3]

        # copia la clave a una temporal para retornarla
        c.execute("INSERT INTO tmpinfo(name, password, nonce, tag) VALUES(?,?,?,?)", (name, site_pass, site_nonce, site_tag,))

        c.execute("SELECT name, password, nonce, tag FROM info WHERE name<>? LIMIT 1", (name,))
        rows=c.fetchall()
        if len(rows) == 0:
            cnn.close()
            return None
        else:
            for row in rows: 
                name_n = row[0]
                site_pass_n = row[1]


        c.execute("UPDATE info SET password =? WHERE name=?", (site_pass_n, name,))

        cnn.commit()

        cnn.close()

    except Error as e: 
        print(e)


def rollback():       
    try:
        #coneccion a la db, la crea si no existe
        cnn = conection(db_file)
        c = cnn.cursor()
        
        c.execute("SELECT name, password FROM tmpinfo LIMIT 1")
        rows=c.fetchall()
        if len(rows) == 0:
            cnn.close()
            return None
        else:
            for row in rows: 
                name_r = row[0]
                site_pass_r = row[1]

        
        c.execute("UPDATE info SET password =? WHERE name=?", (site_pass_r, name_r,))

        c.execute("DROP TABLE tmpinfo")

        cnn.commit()

        cnn.close()

    except Error as e: 
        print(e)
        

actualizar_claves()
#rollback()