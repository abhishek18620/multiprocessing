"""
Author : abhishek18620
Date : 2018-03-21
File : crypto

"""
from cryptography.fernet import Fernet


def ii():
    return int(input())

def mi():
    return map(int, input().split())

def li():
    return list(mi())

def solve():
    key=Fernet.generate_key()
    obj=Fernet(key)
    token=obj.encrypt(b"Hi Its me")
    print(token)
    print(obj.decrypt(token))

if __name__=="__main__":
    solve()
