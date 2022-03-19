# Num1717.py
# https://www.acmicpc.net/problem/1717
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

def Find(a):
    if parent[a] == a: return a
    p = Find(parent[a])
    parent[a] = p
    return parent[a]

def Union(a, b):
    a = Find(a)
    b = Find(b)

    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b



for _ in range(m):
    c, a, b = map(int, input().split())

    if c == 0:
        Union(a, b)
    elif c == 1:
        if Find(a) == Find(b):
            print("YES")
        else:
            print("NO")

    print(parent)