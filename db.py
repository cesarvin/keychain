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
        c.execute("""CREATE TABLE main (salt text);""")
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

def insert_site(site, password,nonce,tag):
    try:
        #coneccion a la db, la crea si no existe
        
        # if (Find_Values(site,1)== None):
        # if (Find_Values(site)== None):
        #     op = input ("El sitio ya existe , desea actualizarlo?(1=si/2=no) ")
        #     if (op==1):
                
        #         cnn = conection(db_file)

        #         c = cnn.cursor()
        #         c.execute("INSERT INTO All_info (name,password,nonce,tag) VALUES(?,?,?,?)", (site,password,nonce,tag))
        #         cnn.commit()

        #         cnn.close()
        #     else:
        #         print ("no se ha modificado ningun registro")
            
        # else:
            cnn = conection(db_file)

            c = cnn.cursor()
            c.execute("INSERT INTO info(name, password, nonce, tag) VALUES(?,?,?,?)", (site, password, nonce, tag,))
            cnn.commit()

            cnn.close()

    except Error as e: 
        print(e)


def search(site, key):       
    try:
        #coneccion a la db, la crea si no existe
        cnn = conection(db_file)
        c = cnn.cursor()

        c.execute("SELECT password, nonce, tag FROM info WHERE name = ? LIMIT 1", (site,))
        rows=c.fetchall()
        for row in rows: 
            site_pass = row[0],row[1],row[2]
            dp = decryptMainPass(site_pass, key)
        #     if (dp.decode("utf-8")==password):
        #         logged = True

        cnn.close()
        return dp.decode("utf-8")

    except Error as e: 
        print(e)

def Delete_values(site):
    
    try:
        
        #coneccion a la db, la crea si no existe
        
        if (Find_Values(site)!= None):
            print ("El sitio no existe")
            return False
        else:
            cnn = conection(db_file)

            c = cnn.cursor()
            c.execute("""DELETE from All_info where Page = ?""", (site,))
            cnn.commit()

            cnn.close()
            print ("Se elimino satisfactoriamente el registro del sitio ", site)
            return True

    except Error as e: 
        print(e)

def insertMainPass(cnn, password):
    try:
        c = cnn.cursor()
        
        c.execute("INSERT INTO main_pass(password,nonce,tag) VALUES(?,?,?)", (password[0], password[1], password[2],))

    except Error as e: 
        print(e)



def login(password):
    logged = False
    try: 
        cnn = conection(db_file)
        c = cnn.cursor()
        #consulta si el password est� en la db
        c.execute("""SELECT password, nonce, tag FROM main_pass""")
        #c.execute("SELECT * FROM main_pass ")
        
        rows = c.fetchall()

        # for row in rows: 
        #     main_pass = row[0],row[1],row[2]
        #     #dp = decryptMainPass(main_pass)
        #     if (dp.decode("utf-8")==password):
        #         logged = True
        
    except Error as e:
        print (e)
    finally:
        if cnn:
            cnn.close()

    return logged
