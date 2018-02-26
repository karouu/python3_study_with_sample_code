n = int(input('input line to present: '))
pre = [1,1]

print(1)
print('1 1')
for i in range(2,n):
    cur = [1,1]
    for j in range(len(pre)-1):
        cur.insert(j+1,pre[j]+pre[j+1])
    print(' '.join(str(i) for i in cur) )
    pre = cur
