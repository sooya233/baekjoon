#Num10870.py

def fibo(num):
    if(num==0): return 0
    elif(num==1):   return 1
    else:   return fibo(num-1)+fibo(num-2)

n = int(input())
print(fibo(n))