#11399번

n = int(input())
a = list(map(int, input().split(" ")))
a.sort()
sum = 0

for i in range(n):
    if i != 0:
        a[i] += a[i-1]
   

for i in a:
    sum += i
    
print(sum)
