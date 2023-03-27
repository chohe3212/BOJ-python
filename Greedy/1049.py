import sys

N,M = map(int,sys.stdin.readline().split())
list1 = []
list2 = []
for i in range(M):
    x,y = map(int,sys.stdin.readline().split())
    list1.append(x)
    list2.append(y)
list1.sort()
list2.sort()

cnt = []
cnt.append( (N//6)*list1[0] + (N%6)*list2[0])
cnt.append (min(list2)*N)
cnt.append((N//6+1)*list1[0])

print(min(cnt))
