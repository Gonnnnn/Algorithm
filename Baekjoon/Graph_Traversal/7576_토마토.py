from collections import deque
import sys
input = sys.stdin.readline

# 가로, 세로
M, N = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

def to_move(y, x):
  global N, M
  dy = [1, 0, -1, 0]
  dx = [0, 1, 0, -1]
  to = []

  for i in range(4):
    new_y = y + dy[i]
    new_x = x + dx[i]
    if 0<=new_y<N and 0<=new_x<M:
      if Map[new_y][new_x] == 0:
        to.append([new_y, new_x])

  return to

q = deque()
for i in range(N):
  for j in range(M):
    if Map[i][j] == 1:
      q.append([i, j])
      Map[i][j] = -1

result = -1
while(q):
  result += 1
  temp_len = len(q)
  for _ in range(temp_len):
    y, x = q.popleft()

    to = to_move(y, x)
    for new_y, new_x in to:
      q.append([new_y, new_x])
      Map[new_y][new_x] = -1

for row in Map:
  if 0 in row:
    result = -1
    break
    
print(result)