# sorting strings list

if __name__ =='__main__':
    n = int(input('how many string you want to sort: '))
    strList = [ input('string: ') for i in range(n) ]
    print(strList)
    while True:
        flag = 0
        for i in range(n-1):
            if strList[i] > strList[i+1]:
                strList[i],strList[i+1] = strList[i+1], strList[i]
                flag += 1
        if flag == 0:
            break

    print(strList)