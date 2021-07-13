num, money = map(int, input().split())
won_list = [0]*10

for i in range(num):
    won_list[i] = int(input())

count = 0
for i in range(num-1, -1, -1):
    count += int(money/won_list[i])
    money = money%won_list[i]
print(count)