"""
Author : abhishek18620
Date : 2018-03-31
File : diffie-hellman.py

"""

from .elliptic import *
from .finitefield.finitefield import FiniteField

import os

class ECDH:
    def generateSecretKey(self,numBits):
        return int.from_bytes(os.urandom(numBits // 8), byteorder='big')


    def sendDH(self,privateKey, generator, sendFunction):
        return sendFunction(privateKey * generator)


    def receiveDH(self,privateKey, receiveFunction):
        return privateKey * receiveFunction()


    def slowOrder(self,point):
        Q = point
        i = 1
        while True:
            if type(Q) is Ideal:
                return i
            else:
                Q = Q + point
                i += 1


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
?!?jedi=0, ?!?                                         (*_*param privateKey*_*, param generator, param sendFunction) ?!?jedi?!?
        self.alicePublicKey = self.sendDH(self.aliceSecretKey, basePoint, lambda x:x)
        print("{0}Public key is : {1}".format(person,self.alicePublicKey))
        #bobPublicKey = sendDH(bobSecretKey, basePoint, lambda x:x)

        self.sharedSecret = self.receiveDH(self.aliceSecretKey, lambda: self.alicePublicKey)
        #sharedSecret2 = receiveDH(aliceSecretKey, lambda: bobPublicKey)
        print("{0}Shared secret is : {1}".format(person,repr(self.sharedSecret)))
        #print('Shared secret is %s == %s' % (sharedSecret1, sharedSecret2))
        #print('extracing x-coordinate to get an integer shared secret: %d' % (sharedSecret1.x.n))

