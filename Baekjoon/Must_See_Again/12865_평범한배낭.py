import sys
input = sys.stdin.readline

N, K = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(N)]
DP = [[0]*(K+1) for _ in range(2)]

for i in range(N):
  weight = things[i][0]
  value = things[i][1]
  for j in range(1, K+1):
    if j < weight:
      DP[i%2][j] = DP[(i+1)%2][j]
    else:
      DP[i%2][j] = max(DP[(i+1)%2][j-weight] + value, DP[(i+1)%2][j])

print(DP[(N+1)%2][-1])