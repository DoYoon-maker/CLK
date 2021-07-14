n = int(input())

def Pibo(i):
    if i==0: return 0
    if i==1: return 1
    else:
        return Pibo(i-1)+Pibo(i-2)

print(Pibo(n))