from string import ascii_uppercase
 
N = int(input())

word = []
for _ in range(N):
    word.append( list(input()) )

alphabet_dic = {}
for i in ascii_uppercase:
    alphabet_dic[i] = 0

for i in word:
    i.reverse()
    for j in range(len(i)) :
        alphabet_dic[i[j]] += 10**j


sort_list = sorted(alphabet_dic.items(),reverse=True, key= lambda x : x[1])

answer = 0
for i in range(9):
    answer += sort_list[i][1] * (9 - i)

print(answer)
