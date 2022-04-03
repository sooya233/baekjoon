# Num11053.py
# https://www.acmicpc.net/problem/11053

import sys
input = sys.stdin.readline

n = int(input())
dp = []

list = list(map(int, input().split()))
dp.append(list)

temp_list= []
for i in range(n):
    temp_list.append(1)

dp.append(temp_list)

for i in range(1, n):
    temp_list = []
    for j in range(i):
        if dp[0][j] < dp[0][i] :
            temp_list.append(dp[1][j])
    if temp_list:
        dp[1][i] = max(temp_list) + 1

# print(max(dp[:][1]))
print(max(dp[1]))

