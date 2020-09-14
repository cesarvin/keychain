from hashlib import sha256
from backports.pbkdf2 import pbkdf2_hmac
import binascii, os
from db import *
from cifrado import *
import os
import os.path
from os import listdir
from os.path import isfile, join
import time
from cifrado import *
import hmac

class Keychain(object):
    def __init__(self):
        self.salt = None
        self.pass_pbkdf2 = None
        self.it = 0
        pass

    def init(self, password):
        #verifica el si existe la db para consultar el salt, sino crea el salt y lo guarda
        isnew = False
        if os.path.isfile(db_file):
            self.salt = get_salt()
            isnew = False
        else:
            self.salt = os.urandom(64)
            save_salt(self.salt)
            isnew = True

        self.it = int(len(self.salt) * len(password) % 2)
        # pbkdf2
        password = password.encode("utf8")
        self.pass_pbkdf2 = pbkdf2_hmac('sha256', password, self.salt, 100000 + 500 * self.it, 32)
        
        if isnew:
            save_main(self.pass_pbkdf2)

    def load(self, password, representation, trustedDataCheck):
        isload = True
        password = password.encode("utf8")
        pass_check = pbkdf2_hmac('sha256', password, self.salt, 100000 + 500 * self.it, 32)
        main_pass = get_mainpass()    
        # print(pass_check)
        # print(main_pass)
        if pass_check != main_pass:
             isload = False

        if trustedDataCheck != None and isload == True: 
            trusted_sha256 = sha256_Hmac(mensaje=representation, llave=self.pass_pbkdf2)
            if trustedDataCheck != trusted_sha256:
                isload = False

        return isload

    def dump(self):
        rows = search_all()
        tuples = {}
        # mete las tuplas en un diccionario value: sitio web, key: password
        for row in rows:
            tuples[row[1]] = row[0]

        tuples_password = sha256_Hmac(mensaje=tuples, llave=self.pass_pbkdf2)
        return tuples, tuples_password


    def set_value(self, value, password):
        site = hash_Sha256(value)
        psw, nonce, tag = encrypt_AES_GCM( password.encode("utf8"), self.pass_pbkdf2 )
        insert_site(site, psw, nonce, tag)

    def get_value(self, value):
        nombre = value
        nombre_cifrado = hash_Sha256(nombre)
        self.site_pass = search_site(nombre_cifrado, self.pass_pbkdf2)
        return self.site_pass

    def remove(self, name):
        nombre = name
        nombre_cifrado = hash_Sha256(nombre)
        delete_site(nombre_cifrado)
        print("Exito! se elimino el sitio")

