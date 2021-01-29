#Num11653.py

def factor(num,i):
    if(num>1):
        if(num%i==0):
            num = num/i
            print(i)
            factor(num,i)
        else:
            factor(num,i+1)

n = int(input())
i = 2
factor(n,i)