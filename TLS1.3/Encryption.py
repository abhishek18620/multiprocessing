"""
Author : abhishek18620
Date : 2018-04-01
File : Encryption.py

"""
from DiffieHellman import diffie-hellman
import cryptography

class DiffieHellman(ECDH):
    def __init__(self,person):
        #generates all
        self.generate(person)
