import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
  x, y, z = map(int, input().split())
  trees[x-1][y-1].append(z)

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

ground = [[5]*N for _ in range(N)]
for year in range(K):
  # spring
  for i in range(N):
    for j in range(N):
      trees[i][j].sort()
      for idx, tree in enumerate(trees[i][j]):
        if tree <= ground[i][j]:
          ground[i][j] -= tree
          trees[i][j][idx] += 1
        else:
          for dead in trees[i][j][idx:]:
            ground[i][j] += int(dead/2)
          trees[i][j] = trees[i][j][:idx]
          break

  # autumn
  for i in range(N):
    for j in range(N):
      for tree in trees[i][j]:
        if tree % 5 == 0:
          for k in range(8):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
              trees[nx][ny].append(1)

  # winter
  for i in range(N):
    for j in range(N):
      ground[i][j] += A[i][j]

result = 0
for row in trees:
  for cell in row:
    result += len(cell)
print(result)