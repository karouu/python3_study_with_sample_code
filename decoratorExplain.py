'''
summirize from https://www.python-course.eu/python3_decorators.php
- function decorators
- class decorators

To be precise, the usage of decorates is very easy, but writing decorators can be complicated,
especially if you are not experienced with decorators and some functional programming concepts.
'''

# functions inside functions
def f():
    def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")

    print("This is the function 'f'")
    print("I am calling 'g' now:")
    g()

f()

def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32

    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!"
    return result

print(temperature(20))


# functions as parameters
def g2():
    print("Hi, it's me 'g2'")
    print("Thanks for calling me")

def f2(func):
    print("Hi, it's me 'f2'")
    print("I will call 'func' now")
    func()
    print( "func's real name is " + func.__name__ )

f2( g2 )

import math
def foo(func):
    print("The function " + func.__name__ + " was passed to foo")
    result = 0
    for x in [1, 2, 2.5]:
        result += func(x)
    return result

print( foo(math.sin) )
print( foo(math.cos) )


# functions returning functions
def f(x):
    def g(y):
        return y + x + 3
    return g

nf1 = f(1)
nf2 = f(3)

print(nf1(1))
print(nf2(1))

print('# create polynomials of degree 2 ')
def polynomial_creator(a, b, c):
    def polynomial(x):
        return a * x**2 + b * x + c
    return polynomial

p1 = polynomial_creator(2, 3, -1)
p2 = polynomial_creator(-1, 2, 1)

for x in range(-2, 2, 1):
    print(x, p1(x), p2(x))

print('# create polynomial for arbitrary degree')
def polynomial_creator( *coefficients ):
    """ coefficients are in the form a_0, a_1, ... a_n """
    def polynomial(x):
        res = 0
        for index, coeff in enumerate(coefficients):
            res += coeff * x** index
        return res
    return polynomial

p1 = polynomial_creator(4)
p2 = polynomial_creator(2, 4)
p3 = polynomial_creator(2, 3, -1, 8, 1)
p4  = polynomial_creator(-1, 2, 1)

for x in range(-2, 2, 1):
    print(x, p1(x), p2(x), p3(x), p4(x))


# decorator example
print('# a simple decorator')
def our_decorator( func ):
    def function_wrapper(x):
        print( "Before calling " + func.__name__ )
        func(x)
        print( "After calling " + func.__name__ )
    return function_wrapper

def foo(x):
    print("Hi, foo has been called with " + str(x))

print("We call foo before decoration:")
foo("Hi")

print("We now decorate foo with f:")
foo = our_decorator(foo)

print("We call foo after decoration:")
foo(42)

print('# the usual syntax for decorators in python')

@our_decorator
def foo2(x):
    print("Hi, foo has been called with " + str(x))

foo2("Hi")

def our_decorator2( func ):
    def function_wrapper(x):
        print( "Before calling " + func.__name__ )
        res = func(x)
        print(res)
        print( "After calling " + func.__name__ )
    return function_wrapper

@our_decorator2
def succ(n):
    return n+1

succ(10)


from math import sin, cos
sin = our_decorator2(sin)
cos = our_decorator2(cos)
for f in [sin,cos]:
    f(3.1415)

# a generalized version of the function_wrapper, which accepts functions with arbitrary parameters
from random import random, randint, choice

def our_decorator3(func):
    def function_wrapper(*args, **kwargs):
        print("Before calling " + func.__name__)

        res = func(*args, **kwargs)
        print(res)

        print("After calling " + func.__name__)
    return function_wrapper

random = our_decorator3(random)
randint = our_decorator3(randint)
choice = our_decorator3(choice)

random()
randint(3, 8)
choice([4, 5, 6])

# use cases
# checking arguments with a decorator
def argument_test_natural_number( f ):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer")
    return helper

@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

for i in range(1,10):
	print(i, factorial(i))

#print(factorial(-1))

# Counting function calls with decorators
def call_counter( func ):
    def helper(x):
        helper.calls += 1
        return func(x)

    helper.calls = 0
    return helper

@call_counter
def succ(x):
    return x + 1

print('succ.calls counter is {}'.format(succ.calls))
for i in range(10):
    succ(i)

print('succ.calls counter is {}'.format(succ.calls))

# decorators which can cope with functions with
# an arbitrary number of positional and keyword parameters.
def call_counter2( func ):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0

    return helper

@call_counter2
def mul1(x, y=1):
    return x*y + 1

mul1(3, 4)
mul1(4)
mul1(y=3, x=2)

print('mul1.call counter is {}'.format(mul1.calls))


# decorators with parameters
def evening_greeting(func):
    def function_wrapper(x):
        print("Good evening, " + func.__name__ + " returns:")
        func(x)
    return function_wrapper

def morning_greeting( func ):
    def function_wrapper(x):
        print("Good morning, " + func.__name__ + " returns:")
        func(x)
    return function_wrapper

@evening_greeting
def foo(x):
    print(42)

foo("Hi")


def greeting( expr ):
    def greeting_decorator( func ):
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            func(x)
        return function_wrapper
    return greeting_decorator

@greeting("καλημερα")
def foo2(x):
    print(42)

foo2("Hi")

def foo3(x):
    print(42)
'''
greeting3 = greeting('Friday today')
foo3 = greeting3(foo3)
foo3('Hi')
'''
foo3 = greeting('Friday today')(foo3)
foo3('Hi')
print(foo3.__name__)

# using wraps from functools
from functools import wraps

def greeting2( func ):
    '''
    function_wrapper.__name__ = func.__name__
    function_wrapper.__doc__ = func.__doc__
    function_wrapper.__module__ = func.__module__
    '''
    @wraps(func)
    def function_wrapper(x):
        """ function_wrapper of greeting """
        print("Hi, " + func.__name__ + " returns:")
        return func(x)

    return function_wrapper


# classes instead of functions
# the __call__ method

class A:
    def __init__(self):
        print("An instance of A was initialized")

    def __call__(self, *args, **kwargs):
        print("Arguments are:", args, kwargs)

x = A()
print("now calling the instance:")
x(3, 4, x=11, y=10)
print("Let's call it again:")
x(3, 4, x=11, y=10)

class Fibonacci:
    def __init__(self):
        self.cache = {}
    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.cache[n]

fib = Fibonacci()

for i in range(15):
    print(fib(i), end=", ")


# using a class as a decorator
def decorator1(f):
    def helper():
        print("Decorating", f.__name__)
        f()
    return helper

@decorator1
def fooo():
    print("inside fooo()")

fooo()


class decorator2:
    def __init__(self, f):
        self.f = f
    def __call__(self):
        print("Decorating", self.f.__name__)
        self.f()

@decorator2
def fooo2():
    print("inside fooo2()")

fooo2()





















































