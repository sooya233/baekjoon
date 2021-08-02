#Num6987.py
from collections import deque

def isable(group):
    ab = True
    win = 0
    lose = 0
    draw = 0
    drawlist = deque()
    for i in range(0,18,3):
        if group[i] + group[i+1] + group[i+2] != 5:
            ab = False
            return ab
        else:
            win += group[i]
            draw += group[i+1]
            lose += group[i+2]
            if group[i+1] != 0:
                drawlist.append(group[i+1])
    if win != lose:
        ab = False
        return ab
    else:
        if draw % 2 != 0:
            ab = False
            return ab
        else:
            if len(drawlist) % 2 == 0:
                return ab
            else:
                if len(drawlist) > 2:
                    return ab
                else:
                    ab =False
                    return ab


def backtracking(x):
    global flag
    if flag:
        return
    if x == 4:
        for i in range(4):
            print(able[i], end=' ')
        flag = True
        return
    else:
        is_able = isable(score[x])
        if is_able:
            able[x] = 1
        else:
            able[x] = 0
        backtracking(x+1)

score = [[0] * 18 for _ in range(4)]
flag = False

for i in range(4):
    score[i] = list(map(int, list(input().split())))

able = [0] * 4
backtracking(0)