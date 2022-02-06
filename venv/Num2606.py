#Num2606.py

graph = {}
n = int(input())
link = int(input())
for i in range(n):
    graph[i+1] = set()

for _ in range(link):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

def bfs(start, network):
    queue = [start]
    while queue:
        for i in graph[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

visited = []
bfs(1, graph)
output = len(visited)
print(output-1)
