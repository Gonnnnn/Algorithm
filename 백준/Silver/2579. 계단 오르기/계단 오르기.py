import sys
input = sys.stdin.readline

n = int(input())
steps = [10000]
for _ in range(n):
  steps.append(int(input()))
DP = [[0, 0] for _ in range(n+1)]
DP[1][0] = steps[1]

def calc(n):
  if(n <= 1):
    return DP[n]
  if(DP[n][0] == 0 and DP[n][1] == 0):
    one_before = calc(n-1)
    two_before = calc(n-2)
    DP[n][0] = max(two_before[0], two_before[1]) + steps[n]
    DP[n][1] = one_before[0] + steps[n]
  return DP[n]

result = calc(n)
print(max(result[0], result[1]))