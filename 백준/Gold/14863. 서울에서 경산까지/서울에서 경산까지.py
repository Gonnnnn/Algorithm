import sys

input = sys.stdin.readline

N, K = map(int, input().split(' '))
# 도보 시간 / 도보 금액 / 자전거 시간 / 자전거 금액
data = [list(map(int, input().split(' '))) for _ in range(N)]
dp = [[0 for _ in range(K + 1)] for _ in range(N)]

for i in range(N):
    walkTime, walkValue, bicycleTime, bicycleValue = data[i]
    if i == 0:
        dp[i][walkTime] = walkValue
        dp[i][bicycleTime] = max(dp[i][bicycleTime], bicycleValue)
    else:
        for j in range(1, K + 1):
            if dp[i - 1][j] == 0: continue
            if j + walkTime <= K:
                dp[i][j + walkTime] = max(dp[i][j + walkTime], dp[i - 1][j] + walkValue)
            if j + bicycleTime <= K:
                dp[i][j + bicycleTime] = max(dp[i][j + bicycleTime], dp[i - 1][j] + bicycleValue)

print(max(dp[N-1]))