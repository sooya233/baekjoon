# Num4963.py
# https://www.acmicpc.net/problem/4963

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(a, b):
    queue = [[a, b]]

    while queue:
        x, y = queue.pop(0)

        for idx in range(8):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < h and 0 <= ny < w and island[nx][ny] == 1:
                island[nx][ny] = 0
                queue.append([nx, ny])

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    island = [[0]*w for _ in range(h)]

    for i in range(h):
        vec = list(map(int, input().split()))
        for j in range(w):
            island[i][j] = vec[j]

    count = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                bfs(i,j)
                island[i][j] = 0
                count += 1
    
    print(count)
