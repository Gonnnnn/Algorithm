import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()
DP = [0]*(k+1)

for i in range(1, k+1):
  Min = k+1
  for coin in coins:
    if coin > i:
      break
    else:
      if DP[i-coin] != -1 and Min > DP[i-coin]:
        Min = DP[i-coin]
  if Min < k+1:
    DP[i] = Min + 1
  else:
    DP[i] = -1

print(DP[-1])