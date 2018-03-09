'''
closure use for:
- replaceing hard coded constants
- eleminating globals
- implementing object orientation
'''

def makeInc(x):
    def inc(y):
        # x is "closed" in the definition of inc
        return y+x
    return inc

'''
Closures in python are created by function calls.
Each call to makeInc creates a new instance of this function,
but each instance has a link to a different binding of x.
'''


class foo:
    def __init__(self, x=0):
        self.x = x

    def update(self):
        print(self.x)
        self.x += 1

f = foo()
g = foo(2)

