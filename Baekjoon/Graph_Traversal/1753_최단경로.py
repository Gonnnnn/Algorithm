import sys
import heapq as hq
input = sys.stdin.readline

# O(NlogN)으로 해결하는 다익스트라
V, E = map(int, input().split())
K = int(input())
INF = sys.maxsize

table = [[] for _ in range(V+1)]
for _ in range(E):
  u, v, w = map(int, input().split())
  table[u].append([v, w])

def D(K):
  global INF

  d = [INF] * (V+1)
  d[K] = 0

  q = []
  hq.heappush(q, [0, K])
  while(q):
    d_closest, idx_closest = hq.heappop(q)

    if d[idx_closest] < d_closest:
      continue
    
    # 가장 가까운 node를 기준으로 d 업데이트
    for node, weight in table[idx_closest]:
      # visit을 따로 만들지 않았었다. 이유는 다음과 같다.
      # 위의 heapq는 거리에 대한 오름차순 정렬을 한다.
      # 현 상태에서 가장 가까운 node를 가져오는 것이다.
      # 이 node를 다른 node를 거쳐서 도달했을 때는 무조건 거쳐가야하는 거리가 더 멀어진다. weight이 양수이기 때문
      # 따라서 해당 코드의 로직에 따라 한번 최초로 처리한 node의 경우 이미 최소 거리이기 때문에 굳이 visit 여부를 따지지 않아도
      # 위의 if문에 의해 알아서 최소 거리를 유지하게 된다.
      
      new_distance = d_closest + weight
      if d[node] > new_distance:
        d[node] = new_distance
        hq.heappush(q, [new_distance, node])
        
  for i in range(len(d)):
    if d[i] == INF:
      d[i] = 'INF'
  for i in d[1:]:
    print(i)

D(K)