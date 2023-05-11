A, B = map(int,input().split())

cnt = 0
while True:
  cnt += 1
  if A == B:
    print(cnt)
    break
  elif A > B :
    print(-1)
    break
  if B % 10 == 1:
    B -= 1
    B = B // 10
  elif B % 2 == 0:
    B = B // 2
  else:
    print(-1)
    break
