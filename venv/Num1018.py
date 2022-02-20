# Num 1018번
# 시작이 0일때, 1일때로 나뉨

def chess(a, b):
    count = [0,0]
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                if chessboard[i+a][j+b] == 1:
                    count[0] += 1
                elif chessboard[i+a][j+b] == 0:
                    count[1] += 1
            elif (i+j)%2==1:
                if chessboard[i+a][j+b] == 0:
                    count[0] += 1
                elif chessboard[i+a][j+b] == 1:
                    count[1] += 1
    #print(count)
    return min(count)

n, m = map(int, input().split())

chessboard = [[0]*m for _ in range(n)]

for i in range(n):
    col = input()
    for j in range(len(col)):
        if col[j] == "B":
            chessboard[i][j] = 1

recolors = []

for i in range(n-7):
    for j in range(m-7):
        recolor = chess(i, j)
        recolors.append(recolor)

#print(recolors)
print(min(recolors))