# /usr/bin/python
# FileName:MyModule.py

class ClassOne:
    count = 110
    name = 'Thursday is raining'

    def __init__(self, name):
        self.name = name
        print('the class name is {}\nthe self name is: {}'.format(ClassOne.name, self.name))

    def getInfo(self, n1):
        self.n1 = n1
        print('get information by self.name, n1: {}'.format(self.n1))


class ModuleClass:
    count = 111

    def __init__(self, name):
        self.name = name
        if __name__ == '__main__':
            print("the module execute by itself")
        else:
            print("the module execute by another soft")

    def getInfo(self, n2,n3):
        self.n2= n2
        self.n3 = n3
        print(self.n2)
        print(self.n3)

'''
m = ModuleClass("Init")
m.getInfo()
'''