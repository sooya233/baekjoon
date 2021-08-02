#Num14888.py
from collections import deque
import copy
from copy import deepcopy

def backtracking(op, result, operations):
    global min_num
    global max_num
    visited.append(op)
    cop_operations = copy.deepcopy(operations)
    cop_operations[op] -= 1

    if op == 0:
        result += numbers[len(visited)]
    elif op == 1:
        result -= numbers[len(visited)]
    elif op == 2:
        result *= numbers[len(visited)]
    elif op == 3:
        if result < 0:
            result = - (abs(result) // numbers[len(visited)])
        else:
            result = result // numbers[len(visited)]

    for i in range(4):
        if cop_operations[i] != 0:
            backtracking(i, result, cop_operations)

    if len(visited) == N-1:
        if result < min_num:
            min_num = result
        if result > max_num:
            max_num = result
        visited.pop()
        return result
    else:
        visited.pop()
        return result


min_num = 1000000000
max_num = -1000000000
N = int(input())
numbers = [0 * N]
numbers = list(map(int, list(input().split())))

operations = [0*4]
operations = list(map(int, list(input().split())))

for i in range(4):
    visited = deque()
    if operations[i] != 0:
        backtracking(i,numbers[0],operations)

print(max_num)
print(min_num)


