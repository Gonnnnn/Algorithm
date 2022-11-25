import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
adj = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    node1, node2 = map(int, input().split(' '))
    adj[node1].append(node2)
    adj[node2].append(node1)

visited = [False for _ in range(N + 1)]
parent = [0 for _ in range(N + 1)]
q = deque([1])

while(q):
    cur = q.popleft()
    for adjNode in adj[cur]:
        if visited[adjNode]: continue
        parent[adjNode] = cur
        visited[adjNode] = True
        q.append(adjNode)

for i in range(2, N + 1):
    print(parent[i])