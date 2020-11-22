#Num1157.py

'''
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.

첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''

alphabet = [0 for i in range(26)]

word = list(input())

for i in word:
    change_ord = ord(i)
    if change_ord<97:
        alphabet[change_ord-65] += 1
    else:
        change_ord -= 32    #소문자를 대문자로 바꾸기
        alphabet[change_ord-65] += 1

max = 0
overlap = 0
index_alphabet = 0
index = 0
for j in alphabet:
    if j>max:
        max = j
        overlap = 0
        index_alphabet = index
        index += 1
    elif j==max:
        overlap = 1
        index += 1
    else:
        index += 1

if(overlap>0):
    print("?")
else:
    print(chr(index_alphabet+65))