# sorting strings list

if __name__ =='__main__':
    n = int(input('how many string you want to sort: '))
    strList = [ input('string: ') for i in range(n) ]
    print('befor sorting: ' + strList)
    #Buble sorting
    while True:
        flag = True
        for i in range(n-1):
            if strList[i] > strList[i+1]:
                strList[i], strList[i+1] = strList[i+1], strList[i]
                flag = False
        if flag:
            break

    print('After sorting: '+strList)