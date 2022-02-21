# Num15650.py
# https://www.acmicpc.net/problem/15650

def bfs(n, m):
    deque = []
    output = []
    for i in range(1, n+1):
        deque.append([i])

    while deque:
        sequence = deque.pop(0)

        if len(sequence) == m:
            output.append(sequence)
            continue

        for i in range(sequence[0], n+1):
            if i in sequence: pass
            else:
                if i > sequence[-1]:
                    new_seq = sequence[:]
                    new_seq.append(i)
                    deque.append(new_seq)

    return output

n, m = map(int, input().split())

result = bfs(n, m)

for i in range(len(result)):
    line = ""
    for j in range(m):
        line += str(result[i][j]) + " "
    print(line)
