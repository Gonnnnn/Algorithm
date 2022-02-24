import sys
import heapq as hq
input = sys.stdin.readline

N = int(input())
# [주유소 위치, 주유 가능 양]
stations = [list(map(int, input().split())) for _ in range(N)]
# 마을 위치, 기존에 있던 연료의 양
L, P = map(int, input().split())
stations.sort(reverse=True)

# 충전할 수 있는 가스. priorityqueue로 구현될 것이라 그 때 그 때 필요하면 충전할 것이다.
q = []
# 멈춘 횟수
result = 0
while(P < L):
  
  while(stations and stations[-1][0] <= P):
    _, g = stations.pop()
    hq.heappush(q, -g)
    
  if not q:
    result = -1
    break

  temp = hq.heappop(q)
  P = P + (-1) * temp
  result += 1

print(result)