N = int(input())
A = list(map(int, input().split()))
DP = [0]*N

for i in range(N):
  Max = 0
  for j in range(i):
    if A[j] > A[i]:
      if Max < DP[j]:
        Max = DP[j]
  DP[i] = Max + 1

print(max(DP))