"""
Author : abhishek18620
Date : 2018-03-30
File : __main__
Doc: http://asyncio.readthedocs.io/en/latest/webscraper.html
"""

import asyncio
import time

class Server:
    ques={
        "what is your name": "Server",
        "what do you do": "I serves authnticated clients"
    }
    def __init__(self):
        print(self.ques)

    def AddQuestion(self ,que ,ans):
        self.ques[que]=ans

if __name__=="__main__":
    server=Server()
