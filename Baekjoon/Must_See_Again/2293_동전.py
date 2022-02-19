import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
# coins.sort()

DP = [0]*(k+1)
DP[0] = 1
for coin in coins:
  for i in range(coin, k+1):
    DP[i] += DP[i-coin]

print(DP[-1])