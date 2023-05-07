import sys
input = sys.stdin.readline

N, M = map(int,input().split())
list1 = list(map(int,input().split()))
sum = 0
list_sum = [0]
for i in list1:
    sum += i
    list_sum.append(sum)

for i in range(M):
    a,b = map(int,input().split())
    print(list_sum[b]-list_sum[a-1])
