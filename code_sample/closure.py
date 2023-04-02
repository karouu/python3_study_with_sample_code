'''
closure use for:
- replaceing hard coded constants
- eleminating globals
- implementing object orientation programming
'''

'''
Closures in python are created by function calls.
Each call to makeInc creates a new instance of this function,
but each instance has a link to a different binding of x.
'''
def makeInc(x):
    def inc(y):
        # x is "closed" in the definition of inc
        return y+x
    return inc

closure = makeInc(5)
for i in range(2,9,2):
    print(closure(i))


class foo:
    def __init__(self, x=0):
        self.x = x

    def update(self):
        print(self.x)
        self.x += 1

f = foo()
for i in range(5):
    f.update()
g = foo(2)
g.update()


