import sys
input = sys.stdin.readline
# 정점, 간선
N, M = map(int, input().split())
table = [[] for _ in range(N+1)]
for _ in range(M):
  u, v = map(int, input().split())
  table[u].append(v)
  table[v].append(u)

visited = [False] * (N+1)
def DFS(u):
  if visited[u]:
    return 0

  visited[u] = True
  for v in table[u]:
    DFS(v)

  return 1

result = 0
for i in range(1, N+1):
  result += DFS(i)

print(result)