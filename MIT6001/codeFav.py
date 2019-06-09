def remainder(x, a):
    """
    the implication of % eperator in python
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        rem(x-a, a)
        
def union(set1,set2):
    """two string arguments, return union part of this two set"""
    if not set1:
        return set2
    elif set1[0] in set2:
        return union(set1[1:],set2)
    else:
        return set1[0]+union(set1[1:],set2)
'''
s1 = 'bcde'
s2 = 'abc'
print(union(s1,s2))
'''

# dealing with Exceptions
''' exception raised by any statement in body of try are handled by
the except statement and execution coutinues after the body of 
the except statement '''
'''
try:
    a = int(input("number a: "))
    b = int(input("number b: "))
    print("a/b = ",a/b)
    print("a+b = ",a+b)
    print("Okay")
except ValueError:
    print("Could not convert to a number")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Something went wrong")
print("Outside")
'''

'''
while True:
    try:
        n = input("Please enter an intger:")
        n = int(n)
        break
    except ValueError:
        print("Input not an integer;try again")
print("Correct input of an integer!")
'''

def fancy_divide1(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")

# try...except...else...finally
def fancy_divide2(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            index = index-1
            fancy_divide(numbers, index)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")

#exception can be overrided
def fancy_divide3(list_of_numbers, index):
    try:
        try:
            raise Exception("what's up")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
            print("finally")
    except Exception as ex:
        print(ex)

def fancy_divide4(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("hey bro")
    except Exception as ex:
        print(ex)

def simple_divide(item, denom):
    try:
        return item/denom
    #Catch a division by zero and return 0
    except ZeroDivisionError as ex:
        print(ex)
        return 0
        
def fancy_divide5(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [simple_divide(item,denom) for item in list_of_numbers]

#print(fancy_divide5([0,2,4], 0))
#fancy_divide2([0,2,4], 1)
#fancy_divide4([0,2,4], 0)

#Assertion
def normalize(numbers):
    max_number = max(numbers)
    
    #pre-condition
    assert (max_number != 0), "Cannot divide by 0"
    
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        
        # post-condition
        assert (0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers 
#normalize([0,0,0])
#AssertionError: Cannot divide by 0

def OddTuple(aTuple):
    length = len(aTuple)
    newTup=()
    for i in range(0, length, 2):
        newTup += (aTuple[i], ) # , is key to garrantte that it's a tuple
    return newTup
#print(OddTuple(['a','b','c','d','e']))

'''
# a program running time
import time

def c2f(c):
    return c*9/5 + 32
    
t0 = time.clock()
c2f(100000000)
t1 = time.clock() - t0
print(t1)

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

t3 = time.clock()
factorial(500)
t4 = time.clock() - t3
print(t4)
'''

def int2Str(n):
    digits = '0123456789'
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        result = digits[n%10] + result
        n = n//10
    return result
#print(int2Str(9999))

'''
# approximation of square root algorithm
x = 26
epsilon = 0.01
step = 0.1
guess = 0.0
count=0
while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step
        count += 1

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('count of guess: '+str(count)+' succeeded: ' + str(guess))

'''
'''
#Bisection(Binary) search algorithm
x = 24
epsilon = 0.01 
numGuesses = 0 
low = 1.0 
high = x 
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon: 
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans)) 
    numGuesses += 1 
    if ans**2 < x: 
        low = ans 
    else: 
        high = ans 
    ans = (high + low)/2.0 
print('numGuesses = ' + str(numGuesses)) 
print(str(ans) + ' is close to square root of ' + str(x))
'''

'''
#0<x<1 cube root
x = 0.008
epsilon = 0.0001
numGuesses = 0 
low = x 
high = 1.0 
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon: 
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans)) 
    numGuesses += 1 
    if ans**3 < x: 
        low = ans 
    else: 
        high = ans 
    ans = (high + low)/2.0 
print('numGuesses = ' + str(numGuesses)) 
print(str(ans) + ' is close to square root of ' + str(x))
'''
'''
input('Please think of a number between 0 and 100! ok?')
low = 1
high = 100
mid=(high+low)//2
while True:
    print("Is your secret number {}?".format(mid))
    judge=input("Enter 'h' to indicate the guess is too high.\
    Enter 'l' to indicate the guess is too low.Enter 'c' to indicate I guessed correctly.")
    if judge == 'h':
        high = mid
    elif judge == 'l':
        low = mid
    elif judge == 'c':
        print("Game over. Your number is {}".format(mid))
        break
    else:
        print("sorry.pls input correct choice")
        continue
    mid = (high+low)//2
'''
'''
# Newton-Raphson algorithm
epsilon = 0.01
y = 24.0
guess = y/2.0
numGuesses = 0
while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/(2*guess))

print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))
'''

#Converting decimal integer to binary
def int2Bin(n):
    binary = ''
    while n > 0:
        binary = str(n%2) + binary
        n = n // 2
    return binary

#print(int2Bin(4095))

'''
#Convert decimal to binary fraction
x = float(input('Enter a decimal number between 0 and 1: '))
p = 0 
while ((2**p)*x)%1 != 0: 
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)) ) 
    p += 1
num = int(x*(2**p))
result = '' 
if num == 0: 
    result = '0' 
    
while num > 0:      # Convert integer to binary
    result = str(num%2) + result 
    num = num//2
    
for i in range(p - len(result)): 
    result = '0' + result
result = result[0:-p] + '.' + result[-p:] 
print('The binary representation of the decimal ' + str(x) + ' is ' + str(result) )
'''

# function arguments: no, one, function as argument
def func_a():
    print("inside func_a")
    
def func_b(y):
    print("inside func_b")
    return y
    
def func_c(z):      # z is function name    
    print("inside func_c")
    return z()
    
print(func_a())
print(func_b(2)+5)
print(func_c(func_a))  #not func_a(),otherwise it will invoke function


def a(x, y, z):         # y, z can be function name
    if x:
        return y
    else:
        return z

def b(q, r):
    return a(q>r, q, r)

#a(3>2,a,b) return function a.    
#print(type(a(3>2,a,b)))

def applyEachTo(L, x):          # L canbe a collection of functions. 
    result = []
    for i in range(len(L)):
        result.append(L[i](x))  #L[i] calls that function with argument x.
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1
    
#print( applyEachTo([inc, square, halve, abs], -3))
#applyEachTo([inc, max], -3)  #error for max()

# variable scope
# can access but can't modify variable outside function [global variable]
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)

def g2(y):
    x = x+1
    return x
#x = 12
#print(g(x))
#g2(x)              #UnboundLocalError


#With global inside funciton, you can modify varible outside function.
#Fibobacci with a dictionary, more efficient, visualize with python tutor
def fib(n, d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib(n-1,d) + fib(n-2,d)
        d[n] = ans
        return ans

def fib2(n):
    global numFibCalls
    numFibCalls += 1
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fib2(n-1)+fib2(n-2)
'''
numFibCalls = 0
d = {1:1,2:2}
print(fib(15,d))
print(numFibCalls)

numFibCalls = 0
print(fib2(15))
print(numFibCalls)
'''


# Towers of Hannoi, multiple recursion inside function
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

#print(Towers(3, 'P1', 'P2', 'P3'))

''' base: int or float.
exp: int >= 0
returns: int or float, base^exp'''

def iterPower(base,exp):
    result = 1
    while exp > 0:
        result = result*base
        exp = exp-1
    return result
    
def recurPower(base, exp):
    if exp == 0:
        return 1
    else:
        return base*recurPower(base, exp-1)

#print(recurPower(2,6))


''' a, b: positive integers
returns: a positive integer, the greatest common divisor of a & b. '''
def gcdIter(a, b):
    tmp = min(a,b)
    while (a%tmp != 0) or (b%tmp != 0):
        tmp -= 1
    return tmp

#print(gcdIter(9,45))

def gcdRecur(a, b):
    if a<b:
        a,b = b,a
    if b == 0:
        return a
    else:
        return gcdRecur(a-b, b)
        
def gcdRecurPro(a, b):
    if b==0:
        return a
    else:
        return gcdRecurPro(b, a%b)
#print(gcdRecur(11, 44))
#print(gcdRecurPro(86, 44))
    
# bisection algorithm    
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: Boolean Value. True if char is in aStr; False otherwise
    '''
    if len(aStr)==0:
        return False
    if len(aStr)==1:
        return char==aStr
        
    mid = len(aStr)//2
    if char < aStr[mid]:
        return isIn(char, aStr[:mid])
    elif char > aStr[mid]:
        return isIn(char, aStr[mid+1:])
    else:
        return True
        
#print(isIn('a','bcdefghijk'))
#print(isIn('f','bcdefghijk'))
#print(isIn('x','bcdefghijk'))
    
def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   # Base case: If aStr is empty, we did not find the char.
   if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
   if len(aStr) == 1:
      return aStr == char

   # Base case: See if the character in the middle of aStr equals the 
   #   test character 
   midIndex = len(aStr)//2
   midChar = aStr[midIndex]
   if char == midChar:
      # We found the character!
      return True
   
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
   elif char < midChar:
      return isIn(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
   else:
      return isIn(char, aStr[midIndex+1:])    

# divide and conquer algorithm
def isPalindrome(s):
    def toChars(s): 
        s = s.lower() 
        ans = '' 
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz': 
                ans = ans + c 
        return ans
    
    def isPal(s):    
        #base case
        if len(s)==0 or len(s)==1:
            return True
        #recursive case
        else:
            return s[0]==s[-1] and isPal(toChars(s[1:-1]))
    
    return isPal(toChars(s))
    
#print(isPalindrome('ab23a   a'))
#print(isPalindrome('a2b b3a'))


#Selection sort Algorithm
def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
            
def selSort2(L):
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            '''
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            '''
            if L[i] > L[j]:
                L[i],L[j] = L[j],L[i]
            j += 1

#Buble sort Algorithm            
def bubleSort(L):
    """ L, list with unique elements """
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                L[j],L[j-1] = L[j-1],L[j]
            
L = [5,100,3,99,4,5,123,1,66,1,1]
#bubleSort(L)
#print(L)

def bublesort2(aL):
    L = aL[:]
    for i in range(len(L)-1):
        for j in range(len(L)-1-i):
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
    return L

print('before sorting: ',L)
print('after sorting: ',bublesort2(L))











