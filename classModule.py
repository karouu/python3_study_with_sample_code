#/usr/bin/python
# FileName:MyModule.py

class classOne:
    count = 110
    name = 'Thursday is raining'
    def __init__(self, name):
        self.name = name 
        print( 'the class name is {}\nthe self name is: {}'.format(classOne.name,self.name ))
    def GetInfo(self, n1 ):
        self.n1 = n1
        print('get information by self.name,n1: {}'.format(self.n1) )


class ModulClass:
    count = 111
    def __init__(self, name):
        self.name = name 
        if(__name__=='__main__'):
            print("the module execute by itself")
        else:
            print("the module execute by another soft")
    def GetInfo(self):
        print(self.name)

m = ModulClass("Init")
m.GetInfo()
                                             
