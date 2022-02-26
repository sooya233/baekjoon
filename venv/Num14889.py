# Num14889.py
# https://www.acmicpc.net/problem/14889

def make_team(n):
    team = []
    sum_list = []
    total_team = set(range(1,n+1))
    for i in range(1, n+1):
        team.append([i])

    while team:
        sub_team = team.pop(0)
        if len(sub_team) == n/2:
            team1 = sub_team
            team2 = list(total_team-set(sub_team))
            sum = calculate_ability(team1, team2)
            sum_list.append(sum)
            continue

        for i in range(sub_team[-1], n+1):
            if i in sub_team: pass
            else:
                temp = sub_team[:]
                temp.append(i)
                team.append(temp)
    
    return sum_list

def calculate_ability(t1, t2):
    result = 0
    sum_t1 = 0
    sum_t2 = 0
    for i in range(len(t1)):
        for j in range(len(t1)):
            sum_t1 += ability[t1[i]][t1[j]]
            sum_t2 += ability[t2[i]][t2[j]]
    result = abs(sum_t1 - sum_t2)
    return result

num = int(input())

ability = [[0] * (num+1) for _ in range(num+1)]

for i in range(num):
    append_list = list(map(int, input().split()))
    new_append_list = [0] + append_list
    ability[i+1] = new_append_list

result = make_team(num)
print(min(result))