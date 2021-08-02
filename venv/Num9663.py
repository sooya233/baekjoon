#Num9663.py
from collections import deque
import copy
from copy import deepcopy

def backtracking(loc):
    global count
    visited.append(loc)

    if (len(visited) == N):
        count += 1
        visited.pop()
        return count

    else:
        x, y = loc[0], loc[1]
        for i in range(N):
            if check(visited, (x+1,i)):
                backtracking((x+1,i))
        visited.pop()

def check(visited, check_loc):
    for i in visited:
        x = i[0]
        y = i[1]
        if check_loc[0] == x:
            return False
        if check_loc[1] == y:
            return False
        if abs(check_loc[0]-x) == abs(check_loc[1]-y):
            return False
    return True

N = int(input())

count = 0
result = 0

for i in range(N):
    visited = deque()
    backtracking((0,i))


print(count)
