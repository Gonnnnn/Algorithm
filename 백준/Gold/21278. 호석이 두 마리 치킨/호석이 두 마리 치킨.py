import sys
import heapq

input = sys.stdin.readline
N, M = map(int, input().split())
table = [[] for _ in range(N)]
for _ in range(M):
    node, neighbor = map(lambda x:int(x) - 1, input().split())
    table[node].append(neighbor)
    table[neighbor].append(node)

def dijk(start1, start2):
    d = [float('inf') for _ in range(N)]
    d[start1] = 0
    d[start2] = 0
    pq = [(0, start1), (0, start2)]
    while(pq):
        distance, building = heapq.heappop(pq)
        if d[building] < distance: continue
        for neighbor in table[building]:
            curDistance = d[neighbor]
            newDistance = distance + 1
            if newDistance < curDistance:
                pq.append((newDistance, neighbor))
                d[neighbor] = newDistance
    return d

building1 = -1
building2 = -1
time = float('inf')
for i in range(N):
    for j in range(i + 1, N):
        d = dijk(i, j)
        tempTime = sum(d) * 2
        if tempTime < time:
            time = tempTime
            building1 = i + 1
            building2 = j + 1
print(building1, building2, time)
