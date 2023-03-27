N = int(input())
list1 =[]
for _ in range(N):
    W = int (input())
    list1.append(W)
list1.sort(reverse=True)
sum = 0
list_result = []
for i in range(len(list1)):
    sum = list1[i]*(i+1)
    list_result.append(sum)
print(max(list_result))
