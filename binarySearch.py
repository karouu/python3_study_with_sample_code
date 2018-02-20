array = [1,7,13,29,38,42,50,63]
k = 13
min = 0
max = len(array)-1
flag = True
while min<=max:
    mid = (min+max)//2
    if k == array[mid]:
        print('find k!! it\'s array[{}]'.format(mid))
        flag = False
        break
    elif k > array[mid]:
        min = mid+1
    else:
        max = mid-1
if flag:
    print('k is not in array')
