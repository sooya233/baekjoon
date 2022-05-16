# Num1874 : 스택 수열
# https://www.acmicpc.net/problem/1874

n = int(input())
count = 0
stack = []
result = []
no_message = False

for i in range(n):
    x = int(input())

    while(count < x):
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        no_message = True
        break

if no_message:
    print("NO")
else:
    print('\n'.join(result))
