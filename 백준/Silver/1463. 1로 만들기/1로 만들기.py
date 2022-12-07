import sys

input = sys.stdin.readline

N = int(input())
if N == 1:
    print(0)
elif N == 2 or N == 3:
    print(1)
else:
    dp = [0 for _ in range(N + 1)]
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    for i in range(4, N + 1):
        temp = float('inf')
        if i % 3 == 0:
            temp = min(temp, dp[i // 3])
        if i % 2 == 0:
            temp = min(temp, dp[i // 2])
        temp = min(temp, dp[i - 1])
        dp[i] = temp + 1
    print(dp[N])