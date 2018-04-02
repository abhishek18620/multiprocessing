"""
Author : abhishek18620
Date : 2018-03-30
File : client.py
"""
from DiffieHellman.elliptic import Point
from client_encryption import EncryptionECDH
import asyncio
import time
import argparse
import pickle

class Client:

    def __init__(self,identity):
        self.identity=identity
        self.loop=asyncio.get_event_loop()
        message=self.initial_message_build()
        client=self.loop.run_until_complete(self.tcp_sender(message,self.loop))
        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            print("Server Stopped...............................\n\n\n")
        self.loop.close()

    def initial_message_build(self):
        """
        generates
        1) secret key
        2) public key
        """
        self.encrypt=EncryptionECDH(self.identity)
        return self.encrypt.extractPublicKey()

    async def tcp_sender(self,message,loop):
        msg1=message
        while True:
            reader,writer= await asyncio.open_connection('127.0.0.1',7777,loop=loop)
            print("Sending message......{0}".format(message))
            # converting object into bytes
            #nonlocal msg1
            #msg1=self.encrypt.extractPublicKey()
            #WARNING : local object not pickleable
            msg=pickle.dumps(msg1)
            writer.write(msg)
            """
            Initially this should be the server's
            public Key which is received key in our case
            """
            data_received=await reader.read(100)
            data=pickle.loads(data_received)
            #call to create client side sharedsecret
            self.encrypt.secretGeneration(self.identity,data)
            await asyncio.sleep(0.5)
        writer.close()

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--identity",type=str,help="--identity for specifying client's identity")
    args=parser.parse_args()
    if args.identity:
        clientobj=Client(args.identity)
