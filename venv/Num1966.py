# Num1966 - 프린터 큐
# https://www.acmicpc.net/problem/1966
from collections import deque

def find_order(order_importance: list, m: int) -> int:
    queue = deque(order_importance[:])

    count = 1
    while queue:
        o, i = queue.popleft()
        if len(queue) == 0:
            return count
        if i >= max([i[1] for i in queue]):
            if o == m:
                return count
            else:
                count += 1
        else:
            queue.append((o, i))


t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    order = [i for i in range(n)]
    order_importance = [i for i in zip(order, importance)]
    
    output = find_order(order_importance, m)
    print(output)