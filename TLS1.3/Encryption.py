"""
Author : abhishek18620
Date : 2018-04-01
File : Encryption.py
"""
from DiffieHellman import diffie_hellman
import cryptography

class EncryptionECDH(diffie_hellman.ECDH):
    def __init__(self,person,receivedKey):
        #generates all
        self.generate(person)
        self.generateSharedSecret(person,receivedKey)

    def extractPublicKey(self):
        return self.getPublic()

    def extractSharedKey(self):
        return self.getSharedSecret()

    def extractSecretKey(self):
        return self.getSecret()
