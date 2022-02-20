# Num15649.py
# https://www.acmicpc.net/problem/15649
from collections import deque

def sequence(n, m):
    queue = deque()
    result = []
    for i in range(1, n+1):
        queue.append([i])

    while queue:
        pop_list = queue.popleft()
        
        if len(pop_list) == m:
            result.append(pop_list)
            continue
        
        for i in range(1, n+1):
            if i in pop_list: pass
            else:
                new_pop_list = pop_list[:]
                new_pop_list.append(i)
                queue.append(new_pop_list)

    return result

n, m = map(int, input().split())

output = sequence(n, m)
for seq in output:
    out = ""
    for j in range(len(seq)):
        out += str(seq[j]) + " "
    print(out)