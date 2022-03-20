# Num11725.py
# https://www.acmicpc.net/problem/11725
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS(tree, start, parent):
    for i in tree[start]:
        if parent[i] == 0:
            parent[i] = start
            DFS(tree, i, parent)

n = int(input())

tree = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

DFS(tree, 1, parent)

for i in range(2, n+1):
    print(parent[i])