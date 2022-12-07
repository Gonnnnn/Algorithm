import sys

input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N + 1)]
optimalRelation = [0 for _ in range(N + 1)]
dp[1] = 0
for i in range(2, N + 1):
    temp = dp[i-1]
    optimal = i-1
    if i % 2 == 0 and dp[i//2] < temp:
        temp = dp[i//2]
        optimal = i//2
    if i % 3 == 0 and dp[i//3] < temp:
        temp = dp[i//3]
        optimal = i//3
    dp[i] = temp + 1
    optimalRelation[i] = optimal

print(dp[N])
idx = N
while(idx != 0):
    print(idx, end=' ')
    idx = optimalRelation[idx]