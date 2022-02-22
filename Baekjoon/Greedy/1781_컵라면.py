dimport sys
import heapq as hq

input = sys.stdin.readline

N = int(input())
# [deadline, num of cup ramen]
table = [list(map(int, input().split())) for _ in range(N)]
table.sort()

result = []
for i in range(N):
  d, ramen = table[i]
  if len(result) < d:
    hq.heappush(result, ramen)
  else:
    if result[0] < ramen:
      hq.heappop(result)
      hq.heappush(result, ramen)

print(sum(result))