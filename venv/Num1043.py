# Num 1043.py
# https://www.acmicpc.net/problem/1043
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def Find(a):
    if parent[a] == a : return a
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


n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

know = list(map(int, input().split()))[1:]

for _ in range(m):
    party = list(map(int, input().split()))[1:]
    #print("party : ", party)

    for i in range(len(party)-1):
        Union(party[i], party[i+1])
    #print(parent)

print(know)
print(parent)