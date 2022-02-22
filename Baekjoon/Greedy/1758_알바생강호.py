import sys
input = sys.stdin.readline

N = int(input())
tips = [int(input()) for _ in range(N)]
tips.sort(reverse=True)

result = 0
for i in range(N):
  if tips[i] > i:
    result += tips[i] - i
  else:
    break
print(result)