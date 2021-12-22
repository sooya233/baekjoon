#11047번

n, k = map(int, input().split(" "))
price = []
for i in range(n):
    price.append(int(input()))
    
price.reverse()

count = 0
i = 0
while k != 0:
    if k >= price[i]:
        count += k // price[i]
        k -= price[i] * (k//price[i])
        i += 1
    else:
        i += 1
        
print(count)
