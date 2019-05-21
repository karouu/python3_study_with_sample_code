# 6.5(a) 
# display a string one character at a time forward and backward.


aString = raw_input('pls enter a string:')

i = len(aString)
j = 0

while j<i:
    print aString[j]
    print aString[i-1-j]
    j += 1
    
