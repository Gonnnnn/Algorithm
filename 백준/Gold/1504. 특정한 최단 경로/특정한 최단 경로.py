import sys
import heapq

def dijk(start):
    d = [float('inf') for _ in range(N + 1)]
    d[start] = 0
    pq = [(0, start)]
    while(pq):
        weight, node = heapq.heappop(pq)
        if d[node] < weight: continue
        
        for neighborWeight, neighbor in table[node]:
            newWeight = weight + neighborWeight
            if d[neighbor] <= newWeight: continue
            d[neighbor] = newWeight
            heapq.heappush(pq, (newWeight, neighbor))
    return d


input = sys.stdin.readline
N, E = map(int, input().split(' '))
table = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split(' '))
    table[a].append((c, b))
    table[b].append((c, a))
v1, v2 = map(int, input().split(' '))

d1 = dijk(1)
d2 = dijk(v1)
d3 = dijk(v2)

answer = min(d1[v1] + d2[v2] + d3[N], d1[v2] + d3[v1] + d2[N])
print(answer if answer != float('inf') else -1)