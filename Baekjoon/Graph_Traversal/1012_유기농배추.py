import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  # 가로, 세로, 배추의 개수
  M, N, K = map(int, input().split())
  Map = [[0]*M for _ in range(N)]
  cab = []

  for _ in range(K):
    x, y = map(int, input().split())
    cab.append([y, x])
    Map[y][x] = 1
  
  def BFS(y_start, x_start):
    global N, M
  
    q = deque()
    q.append([y_start, x_start])
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    while(q):
      y, x = q.popleft()
      for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<N and 0<=nx<M:
          if Map[ny][nx] == 1:
            Map[ny][nx] = 0
            q.append([ny, nx])
  
  result = 0
  for y, x in cab:
    if Map[y][x] == 1:
      BFS(y, x)
      result += 1
  
  print(result)