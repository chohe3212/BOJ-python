import sys
def binary_search(a,n):
    start = 0
    end = len(a)-1
    while start <= end:
        mid = (start + end) //2
        if a[mid] == n:
            return 1
        elif n <= a[mid]:
            end = mid -1
        elif n > a[mid]:
            start = mid +1
    return 0
while True:
    N,M = map(int,sys.stdin.readline().split())
    if N == 0 and M == 0:
        break
    A = []
    cnt = 0
    for _ in range(N):
        a = int(sys.stdin.readline())
        A.append(a)
    for _ in range(M):
        b = int(sys.stdin.readline())
        cnt += binary_search(A,b)
    print(cnt)