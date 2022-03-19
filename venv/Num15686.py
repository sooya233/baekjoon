# Num15686.py
# https://www.acmicpc.net/problem/15686
from itertools import combinations

def left_chicken(c:list, m:int) -> list:
    '''(Explain) 치킨들의 조합을 뽑아주는 함수.
        간단히 combinations으로 구하였지만, raugh하게 구할수도 있음
    '''
    return combinations(c, m)

def measure_distance(h:list, c:tuple) -> int:
    '''(Explain) 치킨거리를 구하는 함수
    '''
    result = 0
    for hou in h:
        temp_list = []
        r1, c1 = hou
        for com in c:
            r2, c2 = com
            temp_list.append(abs(r1-r2) + abs(c1-c2))
        result += min(temp_list)

    # for com in c:
    #     temp_list = []
    #     r2, c2 = com
    #     for hou in h:
    #         r1, c1 = hou
    #         temp_list.append(abs((r1-r2) + (c1-c2)))
    #     result += min(temp_list)
    return result

n, m = map(int, input().split())
house = []
chicken = []

for i in range(n):
    input_list = list(map(int, input().split()))
    for j in range(len(input_list)):
        # 집인 경우, house 행렬에 삽입
        if input_list[j] == 1:
            house.append((i+1, j+1))
        # 치킨집일 경우, chicken 행렬에 삽입
        elif input_list[j] == 2:
            chicken.append((i+1, j+1))

# print(house)
# print(chicken)
comb = left_chicken(chicken, m)

distance = []
for c in comb:
    distance.append(measure_distance(house, c))
print(min(distance))
