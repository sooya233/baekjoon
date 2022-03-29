# Num 12851.py
# https://www.acmicpc.net/problem/12851
import sys
input = sys.stdin.readline

def bfs(n, k):
    queue = [(n, 0)]

    result = []
    min_time = abs(k-n)
    count = 0
    while queue:
        current, time = queue.pop(0)
        if current == k:
            continue
        if time+1 > min_time:
            break

        front = current + 1
        back = current - 1
        jump = current * 2

        if front == k or back == k or jump == k:
            count += 1
            result.append(time+1)
            if time+1 < min_time:
                min_time = time+1
        else:
            if k - current < 0:
                queue.append((current-1, time+1))
            else:
                queue.append((current-1, time+1))
                queue.append((current+1, time+1))
                queue.append((current*2, time+1))

    return min_time, count


n, k = map(int, input().split())

t, c = bfs(n, k)
print(t)
print(c)