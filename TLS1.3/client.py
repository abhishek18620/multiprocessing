"""
Author : abhishek18620
Date : 2018-03-30
File : client.py
"""
from Encryption import EncryptionECDH
import asyncio
import time
import argparse

class Client:

    def __init__(self,identity):
        self.identity=identity
        self.loop=asyncio.get_event_loop()
        message=initial_message_build()
        client=self.loop.run_until_complete(self.coro)
        print("Serving on : {0}".format(server.sockets[0].getsockname()))
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            print("Server Stopped...............................\n\n\n")

    def initial_message_build(self):
        self.encrypt=EncryptionECDH(self.identity,)

    async def handleClient(self,reader,writer):
        data=await reader.read(100)
        message=data.decode()
        peername=writer.get_extra_info("peername")
        print("Received {0} from Peer : {1}".format(message,peername))
        print("Client's Publickey : {0}".format(message))
        """
        almost everythings done with the following call
        will setup all required keys:
        1) publicKey
        2) secretKey
        3) calculates sharedsecretKey
        """
        self.encrypt=EncryptionECDH("Server",message)
        print("Calculating shared secret for server side")
        to_be_sent = self.encrypt.extractPublicKey()
        writer.write(to_be_sent)
        await writer.drain()
        print("Close the client socket")
        writer.close()

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argumentnt("--identity",type=str,help="--identity for specifying client's identity")
    args=parser.parse_args()
    if args.identity:
        clientobj=Client(args.identity)
