class sample2:
    def __init__(self):
        self.z=0

class sample1:
    def __init__(self):
        self.x=2
        self.y=3
        self.z=sample2()

    def __str__(self):
        return "x = {0} and y = {1} and z = {2}".format(self.x,self.y,self.z.z)

    def __getstate__(self):
        state=self.__dict__.copy()
        #removing picklable attributes
        return state

    def __setstate__(self,state):
        self.__dict__.update(state)



