#Num2206.py

from collections import deque
import copy
from copy import deepcopy
dx = [0,0,1,-1]
dy = [1,-1,0,0]

n,m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]

q = deque()
check = [[[-1]*2 for _ in range(m)] for _ in range(n)]

check[0][0][0] = 1
check[0][0][1] = 1
q.append((0,0,True))

while q:
    x, y, broke = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if x == n - 1 and y == m - 1:
                break
            if broke:
                if check[nx][ny][0] == -1:
                    if a[nx][ny] == 0:
                        check[nx][ny][0] = check[x][y][0] + 1
                        q.append((nx, ny, broke))
                    else:
                        broke = False
                        check[nx][ny][1] = check[x][y][0] + 1
                        q.append((nx, ny, broke))
                        broke = True
            else:
                if check[nx][ny][1] == -1:
                    if a[nx][ny] == 0:
                        check[nx][ny][1] = check[x][y][1] + 1
                        q.append((nx, ny, broke))


if check[n-1][m-1][0] == -1 or check[n-1][m-1][1] == -1:
    if check[n-1][m-1][0] == -1 and check[n-1][m-1][1] == -1:
        print(check[n-1][m-1][0])
    else:
        if check[n-1][m-1][0] == -1:
            print(check[n-1][m-1][1])
        else:
            print(check[n - 1][m - 1][0])
else:
    print(min(check[n-1][m-1][1],check[n-1][m-1][0]))