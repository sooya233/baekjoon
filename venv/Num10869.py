import sys
#Num10869.py

from sys import stdin
A,B = stdin.readline().split()
A = int(A)
B = int(B)

if((A>=1 and A<=10000) and (B>=1 and B<=10000)):
    print(A+B)
    print(A-B)
    print(A*B)
    print(A//B)
    print(A%B)