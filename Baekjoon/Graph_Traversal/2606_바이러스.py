import sys
input = sys.stdin.readline

N = int(input())
C = int(input())
table = [[] for _ in range(N+1)]
for _ in range(C):
  a, b = map(int, input().split())
  table[a].append(b)
  table[b].append(a)
visited = [0]*(N+1)

def DFS(node):
  if visited[node]:
    return
  visited[node] = True
  for adj in table[node]:
    if not visited[adj]:
      DFS(adj)
  return

DFS(1)
print(sum(visited)-1)