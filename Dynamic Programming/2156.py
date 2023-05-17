T = int(input())
input_list =[]
for _ in range(T):
  input_list.append(int(input()))

dp = [0]*T

if T == 1:
  dp[0] = input_list[0]
elif T == 2:
  dp[0] = input_list[0]
  dp[1] = input_list[1]+input_list[0]

else:
  dp[0] = input_list[0]
  dp[1] = input_list[1]+input_list[0]
  for i in range(2,T):
    dp[i] = max(input_list[i]+input_list[i-1]+dp[i-3],
              input_list[i]+dp[i-2],dp[i-1])


print(max(dp))
