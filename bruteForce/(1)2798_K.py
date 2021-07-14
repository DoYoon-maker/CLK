from itertools import combinations
N, M = map(int, input().split())
#print(N, M)
Card = list(map(int, input().split()))
#print(Card)

res = list(combinations(Card, 3))
#print(res)
length = len(res)
Cand = []
for i in range(length):
    Cand.append(res[i][0]+res[i][1]+res[i][2])
Cand = sorted(Cand, reverse=True)
#print(Cand)
i = 0
while M<Cand[i]:
    i += 1
print(Cand[i])