import sys
input = sys.stdin.readline

T = int(input())
DP = [0, 1]
for _ in range(T):
  n = int(input())
  while(DP[-1] < n):
    DP.append(DP[-1] + DP[-2])
  result = []
  for i in range(len(DP)-1, -1, -1):
    if n >= DP[i]:
      result.append(DP[i])
      n -= DP[i]
    if n == 0:
      break
  for i in range(len(result)-1, -1 ,-1):
    print(f'{result[i]}', end=' ')
  print('')