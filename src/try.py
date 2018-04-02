"""
Author : abhishek18620
Date : 2018-04-02
File : try.py

"""
import pickle

class sample:

    def __init__(self):
        self.fun("sample")

    #comment
    def fun(self,s):
        self.str=s
        print(self.str)

class child(sample):

    def __init__(self):
        self.fun("child")


if __name__=="__main__":
    sample()
    obj=child()
    objenc=pickle.dumps(obj)
    print(repr(objenc))
    objnew=pickle.loads(objenc)
    objnew.fun("objnew")
