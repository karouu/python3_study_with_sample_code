#in a list, put the max number in the first, put the min number in the last

aL =[101,2,3,4,7,8,1,21,100,54,23,3,43,87,0]
print(aL)
MAX = 0
MIN = len(aL)-1

for i in range(len(aL)):
    if aL[i]>aL[MAX]:
        MAX = i
    if aL[i]<aL[MIN]:
        MIN = i
aL[0],aL[MAX] = aL[MAX],aL[0]
aL[-1],aL[MIN] = aL[MIN],aL[-1]
print(aL)

# hint
print(max(aL))
print(min(aL))