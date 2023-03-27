import sys

N,M = map(int,sys.stdin.readline().split())
list1 = []
for _ in range(M):
    x = int(input())
    list1.append(x)
list1.sort()
price = []
if N < M:
    for i in list1:
        if N < M-list1.index(i):
            price.append(i*N)
        else:
            price.append(i*(M-list1.index(i)))
    print(list1[price.index(max(price))],max(price))
else :
    for i in list1:
        price.append(i*(M-list1.index(i)))
    print(list1[price.index(max(price))],max(price))
