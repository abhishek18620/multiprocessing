"""
Author : abhishek18620
Date : 2018-04-02
File : client_encryption.py
"""
from DiffieHellman.elliptic import *
from DiffieHellman.finitefield.finitefield import FiniteField
from DiffieHellman import diffie_hellman
import cryptography

class EncryptionECDH(diffie_hellman.ECDH):

    def __init__(self,person):
        #generates all
        self.generate(person)

    # overriding generate from ECDH
    """
    generates
    1) secret key
    2) public key
    """
    def generate(self,person): #person just for debugging purposes
        F = FiniteField(3851, 1)
        """
        NOTE: a,b,x,y could be random as well
             Will see it later!!
        """
        # Totally insecure curve: y^2 = x^3 + 324x + 1287
        curve = EllipticCurve(a=F(324), b=F(1287))

        # order is 1964
        basePoint = Point(curve, F(920), F(303))

        self.aliceSecretKey = self.generateSecretKey(8)
        #bobSecretKey = generateSecretKey(8)
        print("{0}Secret key is : {1}".format(person,repr(self.aliceSecretKey)))
        #print('Secret keys are %d, %d' % (self.aliceSecretKey, bobSecretKey))

        self.alicePublicKey = self.sendDH(self.aliceSecretKey, basePoint, lambda x:x)
        print("{0}Public key is : {1}".format(person,self.alicePublicKey))
        #bobPublicKey = sendDH(bobSecretKey, basePoint, lambda x:x)


    def generateSharedSecretKey(self,person,receivedKey):
        self.sharedSecret = self.receiveDH(receivedKey, lambda: self.alicePublicKey)
        #sharedSecret2 = receiveDH(aliceSecretKey, lambda: bobPublicKey)
        print("{0}Shared secret is : {1}".format(person,repr(self.sharedSecret)))
        #print('Shared secret is %s == %s' % (sharedSecret1, sharedSecret2))
        #print('extracing x-coordinate to get an integer shared secret: %d' % (sharedSecret1.x.n))


    def extractPublicKey(self):
        return self.getPublic()

    def extractSharedKey(self):
        return self.getSharedSecret()

    def extractSecretKey(self):
        return self.getSecret()

if __name__=="__main__":
    obj=EncryptionECDH("client")
