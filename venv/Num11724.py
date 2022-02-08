# Num11724번
# https://www.acmicpc.net/problem/11724

def bfs(graph, n):
    queue = [i for i in range(1, n+1)]
    visited = []
    count = 0

    while queue:
        no = True
        num = queue.pop(0)

        if num not in visited:
            visited.append(num)
            for j in graph[num]:
                if j in visited:
                    no = False
                else:
                    queue.remove(j)
                    visited.append(j)
            if no:
                count += 1

    return count

graph = {}
n, m = map(int, input().split())

for i in range(n):
    graph[i+1] = set()

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

output = bfs(graph, n)
print(output)
