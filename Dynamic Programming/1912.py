N = int(input())
num_list = list(map(int,input().split(' ')))

dp = [num_list[0]]
cnt = 0
for i in range(1,len(num_list)):
    dp.append(max(dp[i-1]+num_list[i],num_list[i]))

print(max(dp))
