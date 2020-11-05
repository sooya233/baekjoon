#Num8393.py

'''
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

1부터 n까지 합을 출력한다.
'''

n = int(input())
result = 0

if(n>=1 and n<=10000):
    for i in range(n):
        result = i+1+result
    print(result)