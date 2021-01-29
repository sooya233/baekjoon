#Num2581.py

def isPrime(num):
    count = 0
    for i in range(num,0,-1):
        if num%i == 0:
            count += 1
    if count == 2:
        return 1
    else:
        return 0

m = int(input())
n = int(input())
small = n
sum = 0
for i in range(n,m-1,-1):
    prime = isPrime(i)
    if prime == 1:
        sum += i
        if i<small:
            small = i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(small)
