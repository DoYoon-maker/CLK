N = int(input())
count = 0
i = 666
j = 0
while 1:
    while 1:
        temp = str(i)
        #print(len(temp))
        #print(temp[0], temp[1], temp[2])
        if temp[j]=='6' and temp[j+1]=='6' and temp[j+2]=='6':
            #print(j)
            count += 1
            #print(count)
            break
        j += 1
        if j+2>= len(temp):
            #print("pass")
            break
    if count == N:
        break
    i += 1
    #print(i)
    j = 0
print(i)