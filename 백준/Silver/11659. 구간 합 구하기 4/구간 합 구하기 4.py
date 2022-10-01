import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split(' '))
nums = list(map(int, input().strip().split(' ')))
dp = [0]
for num in nums:
    dp.append(dp[-1] + num)
for _ in range(m):
    i, j = map(int, input().strip().split(' '))
    print(dp[j] - dp[i-1])