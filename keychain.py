from hashlib import sha256
from backports.pbkdf2 import pbkdf2_hmac
import binascii, os
from db import *
import os
import os.path
from os import listdir
from os.path import isfile, join
import time

class Keychain(object):
    def __init__(self):
        pass

    def init(self, password):
        #verifica el si existe la db para consultar el salt, sino crea el salt y lo guarda
        if os.path.isfile(db_file):
            self.salt = get_salt()
        else:
            self.salt = os.urandom(64)
            save_salt(self.salt)
        # pbkdf2
        i = os.O_RANDOM
        password = password.encode("utf8")
        self.pass_pbkdf2 = pbkdf2_hmac('sha256', password, self.salt, 100000 + 500 * i, 32)

    def load(self, password, representation, trustedDataCheck):
        pass

    def dump(self):
        pass

    def set_value(self, value, password):
        pass

    def get_value(self, value, password):
        pass

    def remove(self, name):
        pass

