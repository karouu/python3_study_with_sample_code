array = [1,4,56,23,67,89,45,32,54,63,42,52,18,49,91,72]

print('buble sorting')
array1 = array
while True:
    count = 0
    for i in range(0, len(array1)-1):
        if array1[i]>array1[i+1]:
            tmp = array1[i]
            array1[i] = array1[i+1]
            array1[i+1] = tmp
            count += 1
    if count == 0:
        break
print(array1)

print('inserting sorting')
array2 = array
for i in range(1, len(array2)):
    for j in range(0, i):
        if array2[i]<array2[j]:
            tmp=array2[i]
            for k in range(i,j,-1):
                array2[k] = array2[k-1]
            array2[j]=tmp
print(array2)

print("selection sorting")
array3 = array
for i in range(0, len(array3)-1):
    for j in range(i+1, len(array3)):
        if array3[i] > array3[j]:
            tmp = array3[i]
            array3[i] = array3[j]
            array3[j] = tmp
print(array3)