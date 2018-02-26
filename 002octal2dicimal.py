# method 1
dicimal = 0
octal = input('input a octal numble: ')
for i in range(len(octal)):
    dicimal = dicimal*8 + (ord(octal[i])-ord('0'))
print(dicimal)

# method 2
s = 0
octal2 = reversed(octal)
for idx,num in enumerate(octal2):
    s += int(num)*pow(8,idx)
print(s)

# method 3
s2 = sum( [ int(octal[i])*8**(len(octal)-1-i) for i in range(len(octal)) ])
print(s2)

# method 4
s3 = 0
for i in [ int(octal[-1-i]) * pow(8,i) for i in range(len(octal)) ]:
    s3 += i
print(s3)