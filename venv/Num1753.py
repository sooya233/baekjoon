# Num1753.py
# https://www.acmicpc.net/problem/1753
import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(s):
    distance[s] = 0
    heapq.heappush(heap, (0, s))

    while heap:
        weight, loc = heapq.heappop(heap)

        if distance[loc] < weight:
            continue

        for next_loc, new_weight in graph[loc]:
            next_weight = new_weight + weight
            if distance[next_loc] > next_weight:
                distance[next_loc] = next_weight
                heapq.heappush(heap, (next_weight, next_loc))
    

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)
heap = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])