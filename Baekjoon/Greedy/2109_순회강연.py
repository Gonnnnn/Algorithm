import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
requests = [list(map(int, input().split())) for _ in range(n)]
requests.sort(key=lambda x:x[1])

result = []
for request in requests:
  if request[1] > len(result):
    hq.heappush(result, request[0])
  else:
    if result[0] < request[0]:
      hq.heappop(result)
      hq.heappush(result, request[0])

print(sum(result))