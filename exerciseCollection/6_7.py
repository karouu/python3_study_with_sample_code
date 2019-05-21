#!/usr/bin/env python

#input a number but as a format of string
num_str = raw_input('Enter a number: ')

#shift the string num into int num
num_num = int(num_str)

#give num_num numbers to a list
non_fac_list = range(1,num_num+1)
print "BEFORE:", repr(non_fac_list)

#loop initiate
i = 0

while i < len(non_fac_list):
    
    # notice i, the length of non_fac_list[] changes everytime del functions.
    if num_num % non_fac_list[i] == 0:
        del non_fac_list[i]
        print len(non_fac_list)
    else:    
        i += 1
    
print "AFTER:", repr(non_fac_list)
print "AFTER_00:", non_fac_list
