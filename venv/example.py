#example.py

def printPrime(m,n):
    prime = [True]*(n+1)
    prime[0] = False
    prime[1] = False
    for i in range(2,int(n**0.5)+1):
        if prime[i] is True:
            for j in range(i+i,n+1,i):
                prime[j] = False

    for i in range(m,n+1):
        if prime[i] is True:
            print(i)

m,n = map(int,input().split(" "))
printPrime(m,n)