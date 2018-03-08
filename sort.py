print('buble sorting')
array1 = [1,4,56,23,67,89,45,32,54,63,42,52,18,49,91,72]
while True:
    count = 0
    for i in range(0, len(array1)-1):
        if array1[i]>array1[i+1]:
            '''
            tmp = array1[i]
            array1[i] = array1[i+1]
            array1[i+1] = tmp
            '''
            array1[i],array1[i+1] = array1[i+1],array1[i]
            count += 1
    if count == 0:
        break
print(array1)

print('inserting sorting')
array2 = [1,4,56,23,67,89,45,32,54,63,42,52,18,49,91,72]
for i in range(1, len(array2)):
    for j in range(0, i):
        if array2[i]<array2[j]:
            tmp=array2[i]
            for k in range(i,j,-1):
                array2[k] = array2[k-1]
            array2[j]=tmp
print(array2)
# insert a number in the sorted array
get_n = int(input('input a number: '))
for i in range(len(array2)):
    if get_n < array2[i]:
        array2.insert(i, get_n)
        break
    if i == len(array2)-1:
        array2.append(get_n)
print(array2)

print("selection sorting")
array3 = [1,4,56,23,67,89,45,32,54,63,42,52,18,49,91,72]
for i in range(0, len(array3)-1):
    for j in range(i+1, len(array3)):
        if array3[i] > array3[j]:
            '''
            tmp = array3[i]
            array3[i] = array3[j]
            array3[j] = tmp
            '''
            array3[i],array3[j] = array3[j],array3[i]
print(array3)
