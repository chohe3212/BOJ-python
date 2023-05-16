import sys
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))
A.sort()
def binary_search(a,x): #이분탐색 함수 구현 a : 찾을 리스트,  x : 찾는 값 
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = ( start + end ) // 2
        if x == a[mid]:
            temp = a[mid]
            del a[mid]
            print("A : ",a)
            return temp
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in B:
    print(A.count(binary_search(A, i)), end = " ")
