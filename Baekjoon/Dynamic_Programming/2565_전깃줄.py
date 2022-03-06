import sys
input = sys.stdin.readline

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
table.sort()
DP = [0]*N
for i in range(N):
  temp = 0
  for j in range(i):
    if table[j][1] < table[i][1]:
      if temp < DP[j]:
        temp = DP[j]
  DP[i] = 1 + temp

print(N-max(DP))