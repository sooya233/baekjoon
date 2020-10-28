import sys
#Num1001.py
'''
두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
첫째 줄에 A-B를 출력한다.
'''

'''
A,B = map(int,input().split())
if((A>0 and A<10) and (B>0 and B<10)):
    print(A-B)
'''

'''
A,B = input().split()
A = int(A)
B = int(B)
if((A>0 and A<10) and (B>0 and B<10)):
    print(A-B)
'''

#파이썬 빠른 입출력을 위해선 input() 대신 sys.stdin.readline()을 써야된다고 한다.
from sys import stdin
n = int(stdin.readline())
print(n)
