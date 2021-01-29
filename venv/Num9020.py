#Num9020.py

t = int(input())
for i in range(t):
    num = int(input());

    prime = [True] * (num+1)
    arr = [0,num]
    prime[0] = False
    prime[1] = False

    for j in range(2,int(num**0.5)+1):
        if prime[j] is True:
            for k in range(j+j,num+1,j):
                prime[k] = False

    for j in range(2,num):
        if prime[num-j] is True and prime[j] is True:
            big = num - j
            small = j
            if(big<small): break
            if(arr[1]-arr[0]>big-small):
                arr[1] = big
                arr[0] = small

    print("%d %d" %(arr[0],arr[1]))