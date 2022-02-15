N, M = map(int, input().split())
req = [list(map(int, input().split())) for _ in range(M)]
req.sort(key=lambda x:x[1])

cnt = 0
visited = [False]*(N+1)
for a, b in req:
  for i in range(a, b+1):
    if not visited[i]:
      visited[i] = True
      cnt += 1
      print(visited)
      break

print(cnt)