N = int(input())

list1 = list(map(int, input().split()))

list1.sort()
cnt = 0
sum = 0
for i in list1:
    cnt += i
    sum += cnt
print(sum)