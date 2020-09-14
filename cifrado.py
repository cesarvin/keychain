from Crypto.Cipher import AES
import binascii, os
from hashlib import sha256
import hmac
import random

def encrypt_AES_GCM(value, key):
  aesCipher = AES.new(key, AES.MODE_GCM)
  ciphertext, authTag = aesCipher.encrypt_and_digest(value)
  return (ciphertext, aesCipher.nonce, authTag)
  #return ciphertext

def decrypt_AES_GCM(encrypt_value, key):
  (ciphertext, nonce, authTag) = encrypt_value
  aesCipher = AES.new(key, AES.MODE_GCM, nonce)
  plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
  return plaintext

def encryptMainPass(password, key):
  ecn_pass = encrypt_AES_GCM(password.encode("utf8"), key)
  return ecn_pass

def decryptMainPass(password, key):
  dec_pass = decrypt_AES_GCM(password, key)
  return dec_pass

def hash_Sha256(texto):
  h=sha256()
  h.update(texto.encode())
  return h.hexdigest()

def sha256_Hmac(mensaje, llave):
  return hmac.new(key=bytes(str(llave), encoding='utf-8'), msg=bytes(str(mensaje), encoding='utf-8'), digestmod=sha256).hexdigest()

def get_random():
  s = random.randrange(1000,10000)
  mult = random.randrange(1000,10000)
  inc = random.randrange(1000,10000)
  Modulo = random.randrange(1,5)
  r = (s * mult + inc) % Modulo
  return r
