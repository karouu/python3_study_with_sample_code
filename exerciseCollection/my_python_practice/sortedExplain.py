
# example 1
#给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
#所有的小写字母在大写字母前面
#所有的字母在数字前面
#所有的奇数在偶数前面

#key parameter to specify a function to be called on each list element prior to making comparisons. 
#The value of the key parameter should be a function that takes a single argument and returns a key to use for sorting purposes.
#通俗讲，key 用来决定在排序算法中 cmp 比较的内容，key 可以是任何可被比较的内容，比如元组（python 中元组是可被比较的）。
#lambda 函数将输入的字符转换为一个元组，然后 sorted 函数将根据元组（而不是字符）来进行比较，进而判断每个字符的前后顺序。

s = 'Sorting1234'
"".join( sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(),x) )

#example 2
#sorting last char of the element in a list from small to big according ASCII
"""
def lastchar(chars):
    return chars[-1]
aL = ['abc','b','AAz','ef']
sorted( aL, key =lastchar)
"""

# example 3
# sorting 'age' key in dictionary element of list from small to big

dickList = [ {'name':'nancy','age':21},{'name':'Judy','age':25} ]

def age_sort(aDict):
    return aDict['age']

sorted(dickList, key = age_sort)   #function here has no parentheses()

