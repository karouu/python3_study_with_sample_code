# print prime number in range(n)

#method 1
def prime(n):
	limiter = n//2 +1  # limiter = math.sqrt(n)+1
	flag = False
	'''
	for i in range(2,n):
		if i**2 > n:
			limiter = i
			break
	'''

	for j in range(2,limiter):
		if n%j == 0:
			return flag
	flag =True
	return flag

n =int( input('input a number to find prime bumber: '))
for i in range(2,n):
	if prime(i):
		print(i)

# method 2
print("method 2")
import numpy

def prime2(n):
	num = numpy.arange(n+1)
	for i in num[2:n+1]:
		c =0
		mod1 = []
		mod1.append( numpy.mod(i,num[1:i+1]))
		c = numpy.count_nonzero(mod1)
		if(numpy.size(mod1)-c <= 2):
			print(i)
		
prime2(n)

# method 3
print('method 3')
for i in range(2,n+1):
	if 0 not in [ i%n  for n in range(2,i)]:
		print(i)


# method 4
print('method 4')
a = []
for i in range(2,n):
	for j in range(2,n):
		if i*j <= n:
			a.append(i*j) 

a = set(a)
b = set(range(2,n+1))
c = b-a
print(c)

# method 5
print('method 5')










