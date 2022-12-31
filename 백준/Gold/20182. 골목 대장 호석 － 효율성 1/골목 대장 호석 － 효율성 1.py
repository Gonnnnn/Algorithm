import sys
import heapq

def solve(bar):
    pq = [(0, a)]
    d = [float('inf') for _ in range(n + 1)]
    while(pq):
        weight, node = heapq.heappop(pq)
        if d[node] < weight: continue

        for neighborWeight, neighbor in table[node]:
            if bar < neighborWeight: continue
            newWeight = weight + neighborWeight
            if d[neighbor] <= newWeight: continue
            d[neighbor] = newWeight
            heapq.heappush(pq, (newWeight, neighbor))
    return d[b] <= c

input = sys.stdin.readline
n, m, a, b, c = map(int, input().split(' '))
table = [[] for _ in range(n + 1)]
for _ in range(m):
    first, second, weight = map(int, input().split(' '))
    table[first].append((weight, second))
    table[second].append((weight, first))

answer = -1
for i in range(1, 21):
    if solve(i):
        answer = i
        break
print(answer)