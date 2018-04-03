"""
Author : abhishek18620
Date : 2018-04-02
File : try.py

"""
import pickle
from try2 import sample1

class sample:

    def __init__(self):
        self.fun("sample")

    #comment
    def fun(self,s):
        sampleobj=sample1()
        self.fun1(s,sampleobj)

    def fun1(self,s,sampleobj):
        self.str=s
        if True:
            print(self.str)
            #sample1obj=sample1()
            enc=pickle.dumps(sampleobj)
            print(repr(enc))
            dec=pickle.loads(enc)
            sampleobj.x=55
            sampleobj.y=66
            print(dec)
            print(sampleobj)
class child(sample):

    def __init__(self):
        self.fun("child")


if __name__=="__main__":
    sample()
    # obj=child()
    # objenc=pickle.dumps(obj)
    # print(repr(objenc))
    # objnew=pickle.loads(objenc)
    # objnew.fun("objnew")
