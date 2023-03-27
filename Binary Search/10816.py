import sys
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))
A.sort()
def binary_search(a,x): #이분탐색 함수 구현 a : 찾을 리스트,  x : 찾는 값 
    start = 0
    end = len(a) - 1
    cnt = 0
    while start <= end:
        mid = ( start + end ) // 2
        if x == a[mid]:
            del a[mid]
            end = mid - 1
            cnt += 1

        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return cnt

for i in B:
    print(binary_search(A, i),end = ' ')
