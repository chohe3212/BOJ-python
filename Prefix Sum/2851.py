list1 = []
for _ in range(10):
    a = int(input())
    list1.append(a)

list_under100 = []
a = 0
for i in range(10):
    a += list1[i]
    if a == 100:
        list_under100.append(100)
        break
    elif a < 100:
        list_under100.append(a)
    elif 100 - list_under100[-1] >= a - 100:
        list_under100.append(a)
        break
print(list_under100[-1])

        



