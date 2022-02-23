import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def move(y, x):
  global M, N
  dy = [1, 0, -1 ,0]
  dx = [0, 1, 0 , -1]

  to = []
  for i in range(len(dy)):
    if 0 <= y + dy[i] < M and 0 <= x + dx[i] < N:
      if Map[y+dy[i]][x+dx[i]] < Map[y][x]:
        to.append([dy[i], dx[i]])
  # [[y1, x1],[y2, x2]]
  return to

# 세로, 가로
M, N = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(M)]
DP = [[-1] * N for _ in range(M)]

def DFS(y, x):
  if y == M-1 and x == N-1:
    return 1

  if DP[y][x] >= 0:
    return DP[y][x]

  DP[y][x] = 0

  to = move(y, x)
  if to:
    for dy, dx in to:
      DP[y][x] += DFS(y+dy, x+dx)
  return DP[y][x]
  
print(DFS(0, 0))