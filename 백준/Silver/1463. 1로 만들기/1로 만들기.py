import sys

input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N + 1)]
for i in range(2, N + 1):
    temp = dp[i - 1]
    if i % 3 == 0:
        temp = min(temp, dp[i // 3])
    if i % 2 == 0:
        temp = min(temp, dp[i // 2])
    dp[i] = temp + 1
print(dp[N])