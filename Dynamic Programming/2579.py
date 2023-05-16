N = int(input())

stair_list = []
for _ in range(N):
  stair_list.append(int(input()))

score = [0]*(N)

if N <= 2 :
  print(sum(stair_list))

else:
  score[0] = stair_list[0]
  score[1] = stair_list[1]+ stair_list[0]

  for i in range(2, N):
    score[i] = max(stair_list[i] + stair_list[i-1] + score[i-3],
                  stair_list[i] + score[i-2] )
  print(score[-1])
