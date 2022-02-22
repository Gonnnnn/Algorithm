N = int(input())
numbers = list(map(int, input().split()))

DP = [0]*(N)
DP[0] = numbers[0]
for i in range(N):
  Max = 0
  for j in range(i):
    if numbers[j] < numbers[i]:
      if DP[j] > Max:
        Max = DP[j]
  DP[i] = numbers[i] + Max

print(max(DP))