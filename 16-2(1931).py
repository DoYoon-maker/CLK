c = int(input())

clist = []
for _ in range(0,c):
    clist.append(list(map(int, input().split())))
clist.sort(key=lambda x:(x[1],x[0]))

r = 0
f = 0

for cl in clist:
    if f<=cl[0]:
        f=cl[1]
        r+=1
print(r)