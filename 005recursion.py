# input 'abcde' output 'edcba'
import os
s = input('Input a string: ')

# method 1
def output(s,L):
    if L==0:
       return
    print(s[L-1], end='')
    output(s,L-1)

print('method 1 result')
output(s, len(s))

# method 2
aList = list(s)
aList.reverse()
print('\nmethod 2 result')
for i in range(len(aList)):
	print(aList[i], end='')

# method 3
print('\nmethod 3 result')
for i in range(len(s)-1, -1, -1):
	print(s[i], end='')
print()
