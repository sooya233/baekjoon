# Num1920 - 수 찾기
# https://www.acmicpc.net/problem/1920
# 해법은 단순하지만, 시간때문에 고생한 문제. 이분탐색과 같은 방법을 사용하여 찾는 시간복잡도를 O(logN)으로 줄일 수 있지만, set이나 dict자료형을 사용한다면 시간 복잡도는 O(1)이다.

n = int(input())

a = set(map(int, input().split()))

m = int(input())
result = [0] * m
find = list(map(int, input().split()))
# print(find)

for i in range(m):
    if find[i] in a:
        print(1)
    else:
        print(0)

