from hashlib import sha256
from backports.pbkdf2 import pbkdf2_hmac


class Keychain(object):

    def init(self, password):
        #pbkdf2 Gerearar un password 
        pass
        
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