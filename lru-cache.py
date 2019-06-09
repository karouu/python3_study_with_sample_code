#dynamic programming
#	-overlapping subproblems  memorization
#lru: least recently used 
from functools import lru_cache
import urllib

@lru_cache(maxsize=32)
def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except: #urllib.error.HTTPError:
        return 'Not Found'

for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
    pep = get_pep(n)
    print(n, len(pep))

print(get_pep.cache_info())

@lru_cache(maxsize=None)
def memo_fib(n):
    """Recursively compute fibonacci number with memoization.

    Args:
        n (int): fibonacci nr to be found
    Returns:
        (int): n-th fibonacci number
        memo_fib(5) --> 8
        memo_fib(12) --> 233
    Errors:
        TypeError when n not int or float.
        WARNING: floats give results but are not valid input.
    """
    if n <= 1:
        return 1
    else:
        return memo_fib(n-1) + memo_fib(n-2)

print('memo_fib(n):',
	[memo_fib(n) for n in range(1,64)]
	)

print(memo_fib.cache_info())


def memodict(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        __slots__ = ()
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__

@memodict
def fib(n):
	global n_calls
	n_calls += 1
	if n < 2:
		return n
	return fib(n-1) + fib(n-2)

n_calls = 0
fib(64)
print('n_calls= ',n_calls)
print(fib.__self__)

# 1.define a function called memodict with the parameter f, which will be a function (this is so we can use it as a decorator later)
# 2.create a class with the same name, which inherits from dict (we do this because we want to use the dicts methods (store normal key: value pairs) 
#   and just override its __missing__ method which is activated whenever we get a KeyError)
# 3.inside the memodict class we override the memodict.__missing__ method, which as mentioned is triggered by trying to call a missing key on a dict. 
#   In our own __missing__method we say that if a key is not in the dict we are going to call the function f with the key as argument => f(key) 
#   and store the resulting value both in self as self[key] (this is possible because we inherited from dict) as well as store the result in the variable "ret" 
#   which we will return to the caller. (Basically we just intercepted the function call and made sure to store the value in a dict).
# 4.if the key was not missing we just call memodict().__getitem__. This returns an instance of the memodict class which has not yet been called 
#   (first class objects in Python) to complete the decorator.