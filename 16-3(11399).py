count = int(input())
time_list = list(map(int,input().split()))

time_list.sort()

sum_num = 0
sum_list = [0]*count
for i in range(len(time_list)):
    sum_list[i] = sum(time_list[0:i+1])
print(sum(sum_list))