#Num4948.py

while(True):
    n = int(input())
    count = 0
    if n == 0:  break
    prime = [True] * (2*n+1)
    for i in range(2,int((2*n)**0.5)+1):
        if prime[i] is True:
            for j in range(i+i,2*n+1,i):
                prime[j] = False

    for i in range(n+1,2*n+1):
        if prime[i] is True:
            count += 1

    print(count)