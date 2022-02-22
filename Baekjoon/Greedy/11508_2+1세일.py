import sys
input = sys.stdin.readline

N = int(input())
dairy = [int(input()) for _ in range(N)]

dairy.sort(reverse=True)

result = 0

for i in range(N):
  if (i+1) % 3 != 0:
    result += dairy[i]
  else:
    continue

print(result)