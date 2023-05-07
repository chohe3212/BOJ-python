N = int(input())
cnt = 0
for i in range(1,N+1):
    cnt += i
    if cnt == N:
        print(i)
        break
    elif cnt > N:
        print(i-1)
        break
