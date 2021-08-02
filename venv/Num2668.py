#Num2668.py

def dfs(v, i):
    visited[v] = True
    for w in table[v]:
        if not(visited[w]):
            dfs(w,i)
        elif visited[w] and w == i:
            result.append(w)

N = int(input())
table = [[0] for i in range(N+1)]
for i in range(N):
    table[i+1].append(int(input()))

result = []
for i in range(1,N+1):
    visited = [False] * (N+1)
    dfs(i, i)

print(len(result))
for i in range(len(result)):
    print(result[i])




