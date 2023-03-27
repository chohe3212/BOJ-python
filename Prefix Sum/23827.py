N = int(input())
num_list = list(map(int,input().split()))

sum = sum (num_list)
final_sum = 0

for i in num_list:
    sum -= i
    final_sum =( final_sum + i*sum ) % 1000000007
print(final_sum)
