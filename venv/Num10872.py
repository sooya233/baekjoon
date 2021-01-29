#Num10872.py

def factorial(num):
    if num>1:
        return num * factorial(num-1)
    else :
        return 1

n = int(input())
print(factorial(n))