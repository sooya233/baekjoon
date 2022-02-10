'''
# Num7562.py
from collections import deque

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

def bfs(s):
    count = 0
    s.append(count)
    queue = deque()
    queue.append(s)
    visited = []

    while queue:
        x, y, c = queue.popleft()
        if board[x][y] == 1: return c
        for i in range(8):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0<=n_x<l and 0<=n_y<l and [n_x, n_y] not in visited:
                visited.append([n_x, n_y])
                queue.append([n_x, n_y, c+1])

T = int(input())
for _ in range(T):
    l = int(input())
    board = [[0]*l for _ in range(l)]
    start = list(map(int, input().split()))
    target_x, target_y = map(int, input().split())
    board[target_x][target_y] = 1
    output = bfs(start)
    print(output)
    '''

from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
def bfs(sx, sy, ax, ay):
    q = deque()
    q.append([sx, sy])
    s[sx][sy] = 1
    while q:
        a, b = q.popleft()
        if a == ax and b == ay:
            print(s[ax][ay] -1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and s[x][y] == 0:
                q.append([x, y])
                s[x][y] = s[a][b] + 1
t = int(input())
for i in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    ax, ay = map(int, input().split())
    s = [[0] * n for i in range(n)]
    bfs(sx, sy, ax, ay)