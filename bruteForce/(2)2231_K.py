import sys
N = int(input())

def Sum(num):
    temp = num
    sum = num
    for i in range(len(str(num))):
        sum += temp % 10
        temp = temp // 10
    return sum

i = 1
while 1:
    if Sum(i)==N:
        print(i)
        sys.exit()
    if i==N:
        print(0)
        sys.exit()
    i += 1