"""
Author : abhishek18620
Date : 2018-03-30
File : __main__.py
Doc: http://asyncio.readthedocs.io/en/latest/webscraper.html
"""
from Encryption import EncryptionECDH
import asyncio
import time
import pickle

class Server:
    ques={
        "what is your name": "Server",
        "what do you do": "I serves authnticated clients"
    }

    def __init__(self):
        print(self.ques)
        self.loop=asyncio.get_event_loop()
        self.coro=asyncio.start_server(self.handleClient,'127.0.0.1',7777,loop=self.loop)
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
        message=pickle.dumps(data)
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
        to_be_sent = pickle.loads(self.encrypt.extractPublicKey())
        writer.write(to_be_sent)
        await writer.drain()
        print("Close the client socket")
        writer.close()

if __name__=="__main__":
    serverobj=Server()
