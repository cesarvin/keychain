import sqlite3
from sqlite3 import Error
import binascii, os
from cifrado import *

db_file = 'storage.db'

def conection(db_file):
    cnn = None
    try: 
        #coneccion a la db, la crea si no existe
        cnn = sqlite3.connect(db_file)
        return cnn

    except Error as e:
        print (e)
    return cnn


def createSystemTables(cnn):
    try: 
        #coneccion a la db, la crea si no existe
        c = cnn.cursor()
        #crea la tabla para la clave principal
        c.execute("""CREATE TABLE main (salt text, mainpass text NULL);""")
        c.execute("""CREATE TABLE info (name text,password text, nonce text, tag text);""")

    except Error as e:
        print (e)

def save_salt(sp):
    try: 
        #coneccion a la db, la crea si no existe
        cnn = conection(db_file)
        createSystemTables(cnn)
        insert_salt(cnn, sp)
        cnn.commit()
        cnn.close()

    except Error as e:
        print (e)
    finally:
        if cnn:
            cnn.close()

def insert_salt(cnn, sp):
    try:
        c = cnn.cursor()
        c.execute("INSERT INTO main(salt) VALUES(?)", (sp,))
    except Error as e: 
        print(e)

def get_salt():
    try: 
        cnn = conection(db_file)
        c = cnn.cursor()
        c.execute("""SELECT salt FROM main LIMIT 1""")
        rows = c.fetchall()
        
        for row in rows: 
            salt = row[0]
        
    except Error as e:
        print (e)
    finally:
        if cnn:
            cnn.close()
    return salt

def insert_site(site, password, nonce, tag, key=None):
    try:
        #coneccion a la db, la crea si no existe
        
        if (search_site(site, key) == None):
            cnn = conection(db_file)

            c = cnn.cursor()
            c.execute("INSERT INTO info(name, password, nonce, tag) VALUES(?,?,?,?)", (site, password, nonce, tag,))
            cnn.commit()

            cnn.close()
            print("Se guardo correctamente el sitio y la contraseña!")
            
        else:
            cnn = conection(db_file)
            print("El sitio ya existe")
            c = cnn.cursor()
            c.execute("UPDATE info SET password =?, nonce=?, tag=? WHERE name=?", (password, nonce, tag, site,))
            cnn.commit()
            print("Se actualizo correctamente el sitio y la contraseña!")
            cnn.close()

    except Error as e: 
        print(e)

def delete_site(site, key=None):
    try:
        if(search_site(site, key) == None):
            print("El sitio no existe")
        else:
            #coneccion a la db, la crea si no existe
            cnn = conection(db_file)
            c = cnn.cursor()

            c.execute("DELETE FROM info WHERE name = ?", (site,))
            print("Exito! se elimino el sitio")
            
            cnn.commit()

            cnn.close()

    except Error as e: 
        print(e)


def search_site(site, key):       
    try:
        #coneccion a la db, la crea si no existe
        cnn = conection(db_file)
        c = cnn.cursor()

        c.execute("SELECT password, nonce, tag FROM info WHERE name = ? LIMIT 1", (site,))
        rows=c.fetchall()
        if len(rows) == 0:
            cnn.close()
            return None
        else:
            for row in rows: 
                site_pass = row[0],row[1],row[2]
                dp = decryptMainPass(site_pass, key)
            #     if (dp.decode("utf-8")==password):
            #         logged = True

            cnn.close()
            return dp.decode("utf-8")

    except Error as e: 
        print(e)

def search_all():       
    try:
        #coneccion a la db, la crea si no existe
        cnn = conection(db_file)
        c = cnn.cursor()

        c.execute("SELECT name, password, nonce, tag FROM info ")
        rows=c.fetchall()
       
        cnn.close()
        return rows

    except Error as e: 
        print(e)        


def save_main(mp):
    try:
        cnn = conection(db_file)
        c = cnn.cursor()

        c.execute("UPDATE main SET mainpass = ? WHERE 1=1", (mp,))
        
        cnn.commit()
        cnn.close()
    except Error as e: 
        print(e)

def get_mainpass():
    try: 
        cnn = conection(db_file)
        c = cnn.cursor()
        c.execute("""SELECT mainpass FROM main LIMIT 1""")
        rows = c.fetchall()
        
        for row in rows: 
            mainpass = row[0]
        
    except Error as e:
        print (e)
    finally:
        if cnn:
            cnn.close()
    return mainpass        