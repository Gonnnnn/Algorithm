N, K = map(int, input().split())
DP = [[0] * (N+1) for _ in range(K)]
for i in range(N+1):
  DP[0][i] = 1

for i in range(1, K):
  for j in range(N+1):
    DP[i][j] = sum(DP[i-1][:j+1])%1000000000

print(DP[-1][-1])