'''
有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
'''
# method 1
from collections import deque
n = int(input(' how many people in the circle: '))
circle = [i for i in range(1,n+1)]

de = deque(circle)
print(circle)
while True:
    de.remove(de[2])
    de.rotate(-2)
    if len(de)==2:
        print(de[1])
        break

# method 2
i = 1
while len(circle)>1:
    if i%3 ==0:
        circle.pop(0)
    else:
        circle.insert(len(circle), circle.pop(0))
    i += 1
print(circle[0])

# method 3
i = 0
flag = 1
ruler = 0

while flag < len(circle):
    if circle[i] != 0:
        ruler += 1

    if ruler==3:
        circle[i] =0
        flag += 1
        ruler = 0
    i += 1
    if i ==n:
        i = 0

while circle[i]==0:
    i += 1
print(circle[i])

# method 4
s4 = 0
while True:
    t = 0
    for i in range(len(circle)):
        s4 += 1
        if s4%3 == 0:
            circle.pop(i-t)
            t += 1
    if(len(circle)==1):
        print(circle[0])
        break









