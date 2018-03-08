class test:
    name = 'lily'

    def __init__(self, age):
        self.age = age
        print('{} age is {}'.format(test.name, self.age))

class Base(object):
    def __init__(self):
        print("Base created")

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()

ChildA()
ChildB()

class Animals:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print('Hello, I am %s.' % self.name)

class Dog(Animals):
    def greet(self):
        super(Dog, self).greet()
        print('Wangwang....')

class BaseClass(object):
    def __init__(self):
        print('enter BaseClass')
        print('leave BaseClass')

class A(BaseClass):
    def __init__(self):
        print('enter A')
        super(A, self).__init__()
        print('leave A')
class B(BaseClass):
    def __init__(self):
        print('enter B')
        super(B, self).__init__()
        print('leave B')

class C(B,A):
    def __init__(self):
        print('enter C')
        super(C, self).__init__()
        print('leave C')




