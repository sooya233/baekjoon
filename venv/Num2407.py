# Num2407.py
# https://www.acmicpc.net/problem/2407

n, m = map(int, input().split())

total_1 = 1
for i in range(1, n+1):
    total_1 *= i

total_2 = 1
for i in range(1, m+1):
    total_2 *= i

total_3 = 1
for i in range(1, (n-m)+1):
    total_3 *= i

print(total_1 // (total_2*total_3))