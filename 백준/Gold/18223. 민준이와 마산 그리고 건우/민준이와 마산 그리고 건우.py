import sys
import heapq

def dijk(pq, d):
    while(pq):
        weight, node = heapq.heappop(pq)
        if weight > d[node]: continue

        d[node] = weight
        for neighbor, neighborWeight in table[node]:
            newWeight = weight + neighborWeight
            if newWeight < d[neighbor]:
                d[neighbor] = newWeight
                heapq.heappush(pq, (newWeight, neighbor))

input = sys.stdin.readline
# 정점, 간선, 건우 위치
V, E, P = map(int, input().split(' '))
table = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, w = map(int, input().split(' '))
    table[s].append((e, w))
    table[e].append((s, w))

d1 = [float('inf') for _ in range(V + 1)]
d1[1] = 0
pq1 = [(0, 1)]
d2 = [float('inf') for _ in range(V + 1)]
d2[P] = 0
pq2 = [(0, P)]

dijk(pq1, d1)
dijk(pq2, d2)

print("SAVE HIM" if d1[V] == d1[P] + d2[V] else "GOOD BYE")