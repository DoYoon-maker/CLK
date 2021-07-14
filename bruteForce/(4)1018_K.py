N, M = map(int, input().split())
Board = []
for i in range(N):
    Board.append(input())
#print(Board)
count = []
Chess = []
for k in range(0, M-7):
    for j in range(0, N-7):
        for i in range(j, j+8):
            Chess.append(Board[i][k:k+8])
        #print(Chess)
        temp = 0
        temp2 = 1
        if Chess[0][0] == 'B':
            for p in range(0, 8, 2):
                for q in range(0, 8, 2):
                    if Chess[p][q] != 'B':
                        temp += 1
                    if Chess[p][q+1] != 'W':
                        temp += 1
                    if Chess[p+1][q] != 'W':
                        temp += 1
                    if Chess[p+1][q+1] != 'B':
                        temp += 1
            for p in range(0, 8, 2):
                for q in range(0, 8, 2):
                    if Chess[p][q] != 'W':
                        if p != 0 or q != 0:
                            temp2 += 1
                    if Chess[p][q + 1] != 'B':
                        temp2 += 1
                    if Chess[p + 1][q] != 'B':
                        temp2 += 1
                    if Chess[p + 1][q + 1] != 'W':
                        temp2 += 1
        if Chess[0][0] == 'W':
            for p in range(0, 8, 2):
                for q in range(0, 8, 2):
                    if Chess[p][q] != 'W':
                        temp += 1
                    if Chess[p][q+1] != 'B':
                        temp += 1
                    if Chess[p+1][q] != 'B':
                        temp += 1
                    if Chess[p+1][q+1] != 'W':
                        temp += 1
            for p in range(0, 8, 2):
                for q in range(0, 8, 2):
                    if Chess[p][q] != 'B':
                        if p != 0 or q != 0:
                            temp2 += 1
                    if Chess[p][q+1] != 'W':
                        temp2 += 1
                    if Chess[p+1][q] != 'W':
                        temp2 += 1
                    if Chess[p+1][q+1] != 'B':
                        temp2 += 1
        Chess.clear()
        count.append(min(temp, temp2))
print(min(count))