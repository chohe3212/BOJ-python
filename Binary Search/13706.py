N = int(input())
start = 0
end = N
while start <= end:
    mid = (start + end) //2
    if mid * mid == N:
        print(mid)
        break
    elif mid * mid > N:
        end = mid - 1
    elif mid * mid <= N :
        start = mid + 1