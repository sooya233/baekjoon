# Num1003.py
# https://www.acmicpc.net/problem/1003

def fibo(x):
    if x == 0:
        return dp[0]
    if x == 1:
        return dp[1]
    if dp[x][0] != 0 or dp[x][1] !=0:
        return dp[x]
    dp[x][0] = fibo(x-1)[0] + fibo(x-2)[0]
    dp[x][1] = fibo(x-1)[1] + fibo(x-2)[1]
    return dp[x]

t = int(input())

dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(t):
    n = int(input())
    output = fibo(n)
    print(str(output[0]) + " " + str(output[1]))