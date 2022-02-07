#Num1012.py
dx = [0,0,1,-1]
dy = [1,-1,0,0]

T = int(input())

def bfs(a, b):
    queue = [[a,b]]
    while queue:
        t_x, t_y = queue.pop(0)
        print(f"({t_x}, {t_y})")
        #loc[t_x][t_y] = 0
        for idx in range(4):
            n_x = t_x + dx[idx]
            n_y = t_y + dy[idx]
            if 0<=n_x<N and 0<=n_y<M and loc[n_x][n_y] == 1:
                loc[n_x][n_y] = 0
                queue.append([n_x, n_y])

for _ in range(T):
    count = 0
    M, N, C = map(int, input().split())
    loc = [[0]*M for _ in range(N)]

    for _ in range(C):
        y, x = map(int, input().split())
        loc[x][y] = 1

    for n in range(N):
        for m in range(M):
            if loc[n][m] == 1:
                bfs(n, m)
                loc[n][m] = 0
                count += 1
    
    print(count)
