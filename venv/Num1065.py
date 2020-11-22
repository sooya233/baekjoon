#Num1065.py

'''
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
'''

def h(num):
    han = 0
    for i in range(1,num+1):
        a = list(map(int,str(i)))
        if i < 100:
            han += 1
        else:
            dif1 = a[0] - a[1]
            dif2 = a[1] - a[2]
            if dif1 == dif2:
                han += 1

    return han

n = int(input())
if n<=1000:
    result = h(n)
