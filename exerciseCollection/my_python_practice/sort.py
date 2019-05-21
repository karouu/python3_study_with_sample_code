#!/usr/bin/python

#给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：

#所有的小写字母在大写字母前面
#所有的字母在数字前面
#所有的奇数在偶数前面

#key parameter to specify a function to be called on each list element prior to making comparisons. The value of the key parameter should be a function that takes a single argument and returns a key to use for sorting purposes.

#通俗讲，key 用来决定在排序算法中 cmp 比较的内容，key 可以是任何可被比较的内容，比如元组（python 中元组是可被比较的）。

# example 1
s = 'Sorting1234'
"".join( sorted(s, key=lambda x: (x.isdigit(),x.isdigit() and in(x)%2==0,x.isupper(),x.islower(),x) )


#lambda 函数将输入的字符转换为一个元组，然后 sorted 函数将根据元组（而不是字符）来进行比较，进而判断每个字符的前后顺序。

# example 2
#按列表e中每个元素的最后一个字母的ascii码从小到大排序 
def lastchar(s):
    return s[-1]

e =['abc','b','AAz','ef']
sorted( e, key =lastchar)

# example 3
# 自定义函数按 列表中 的 字典 元素中 age 键 从小到大排序

f = [ {'name':'nancy','age':21},{'name':'Judy','age':25} ]

def age_sort(aDict):
    return aDict['age']

sorted(f, key = age_sort)  # function here has no ()

