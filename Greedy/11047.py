N,K=map(int,input().split())
list1 = []
for _ in range(N):
    a=int(input()) # 동전의 가치 input
    list1.append(a) 
list1.reverse() # 큰 가치부터 계산해야 최솟값이 나와서
cnt = 0
for i in list1:
    if K == 0:
        break
    cnt += K//i # 동전 갯수 더하기
    K = abs(K % i) # -가 나올 수 있으니 절댓값으로
    # K원을 큰 가치 순으로 나눈 나머지를 다시 K에 저장
print(cnt) # 갯수 출력
