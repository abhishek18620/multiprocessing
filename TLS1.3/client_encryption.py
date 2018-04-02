"""
Author : abhishek18620
Date : 2018-04-02
File : client_encryption.py
"""
#from DiffieHellman.elliptic import *
#from DiffieHellman.finitefield.finitefield import FiniteField
from DiffieHellman import diffie_hellman
import cryptography

class EncryptionECDH(diffie_hellman.ECDH):

    def __init__(self,person):
        #generates all
        self.generate(person)


    def secretGeneration(self,person,receivedKey):
        self.generateSharedSecret(person,receivedKey)


    def extractPublicKey(self):
        return self.getPublic()

    def extractSharedKey(self):
        return self.getSharedSecret()

    def extractSecretKey(self):
        return self.getSecret()
