#Num2580.py
from collections import deque


def backtracking(location):
    new_location = deque()
    check1 = [0] * 10  # 가로
    check2 = [0] * 10  # 세로
    check3 = [0] * 10  # 3*3칸
    if len(location) == 0:
        return

    while location:
        loc = location.popleft()
        x, y = loc[0], loc[1]

        for i in range(9):
            check1[sudoku[x][i]] += 1
            check2[sudoku[i][y]] += 1
        for i in range(3):
            for j in range(3):
                if x // 3 == 0 and y // 3 == 0:
                   check3[sudoku[i][j]] += 1
                elif x // 3 == 0 and y // 3 == 1:
                    check3[sudoku[i][j + 3]] += 1
                elif x // 3 == 0 and y // 3 == 2:
                    check3[sudoku[i][j + 6]] += 1
                elif x // 3 == 1 and y // 3 == 0:
                    check3[sudoku[i + 3][j]] += 1
                elif x // 3 == 1 and y // 3 == 1:
                    check3[sudoku[i + 3][j + 3]] += 1
                elif x // 3 == 1 and y // 3 == 2:
                    check3[sudoku[i + 3][j + 6]] += 1
                elif x // 3 == 2 and y // 3 == 0:
                    check3[sudoku[i + 6][j]] += 1
                elif x // 3 == 2 and y // 3 == 1:
                    check3[sudoku[i + 6][j + 3]] += 1
                elif x // 3 == 2 and y // 3 == 2:
                    check3[sudoku[i + 6][j + 6]] += 1

        if check1[0] == 1:
            for i in range(1, 10):
                if check1[i] == 0:
                    num = i
            sudoku[x][y] = num
            backtracking(location)
        else:
            if check2[0] == 1:
                for i in range(1, 10):
                    if check2[i] == 0:
                        num = i
                sudoku[x][y] = num
            else:
                if check3[0] == 1:
                    for i in range(1, 10):
                        if check3[i] == 0:
                            num = i
                    sudoku[x][y] = num
                else:
                    new_location.append((x, y))
    backtracking(new_location)
    return



sudoku = [[0]*9 for _ in range(9)]
location = deque()

for i in range(9):
    sudoku[i] = list(map(int, list(input().split())))

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            location.append((i,j))

#print(location)
backtracking(location)
for i in range(9):
    for j in range(9):
        print(sudoku[i][j], end=' ')
    print()