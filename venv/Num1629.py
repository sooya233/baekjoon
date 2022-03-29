# Num1629.py
# https://www.acmicpc.net/problem/1629

import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

# devide and conqure
def check(a, b):
    if(b == 1):
        return a%c
    elif(b % 2 == 0):
        y = check(a, b//2)
        return y*y%c
    else:
        y = check(a, (b-1)//2)
        return y*y*a%c
        
print(check(a, b))