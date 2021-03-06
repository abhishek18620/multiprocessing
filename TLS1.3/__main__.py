"""
Author : abhishek18620
Date : 2018-03-30
File : __main__.py
Doc: http://asyncio.readthedocs.io/en/latest/webscraper.html
"""
from DiffieHellman.finitefield.finitefield import FiniteField
from DiffieHellman.elliptic import *
from Encryption import EncryptionECDH
import asyncio
import time
import pickle
import argparse

class pickleable:

    def __init__(self,x,y,identity):
        self.x=int(x)
        self.y=int(y)
        self.identity=identity

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


class Server:
    ques={
        "what is your name": "Server",
        "what do you do": "I serves authnticated clients"
    }

    def __init__(self,host):
        print(self.ques)
        self.host=host
        self.loop=asyncio.get_event_loop()
        self.coro=asyncio.start_server(self.handleClient,self.host,7777,loop=self.loop)
        server=self.loop.run_until_complete(self.coro)
        print("Serving on : {0}".format(server.sockets[0].getsockname()))
        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            print("Server Stopped...............................\n\n\n")

    def AddQuestion(self ,que ,ans):
        self.ques[que]=ans

    async def handleClient(self,reader,writer):
        data=await reader.read(100)
        #data should be a pickleable object
        messagetemp=pickle.loads(data)
        #message is a Point object
        client=messagetemp.identity
        message=self.pickleableToPoint(messagetemp)
        peername=writer.get_extra_info("peername")
        print("Received {0} from Peer : {1}".format(message,client))
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
        tempkey=self.encrypt.extractPublicKey()
        to_be_sent_temp=pickleable(tempkey.x , tempkey.y, client)
        to_be_sent = pickle.dumps(to_be_sent_temp)
        writer.write(to_be_sent)
        await writer.drain()
        print("Close the client socket")
        writer.close()


    #converts pixckleable to Point
    def pickleableToPoint(self,obj):
        F=FiniteField(3851,1)
        curve=EllipticCurve(a=F(324),b=F(1287))
        return Point(curve,F(obj.x),F(obj.y))


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--host",type=str,help="server you want to connect")
    args=parser.parse_args()
    if args.host:
        serverobj=Server(args.host)
