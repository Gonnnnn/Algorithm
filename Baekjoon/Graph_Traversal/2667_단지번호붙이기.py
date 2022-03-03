import sys
input = sys.stdin.readline

N = int(input())
Map = [list(input().strip()) for _ in range(N)]

def to_move(y, x):
  global N
  dy = [1, 0, -1, 0]
  dx = [0, 1, 0, -1]
  to = []

  for i in range(4):
    new_y = y + dy[i]
    new_x = x + dx[i]
    if 0<=new_y<N and 0<=new_x<N:
      if Map[new_y][new_x] == '1':
        to.append([new_y, new_x])

  return to

def dfs(y, x):
  global num
  if Map[y][x] == '0':
    return

  Map[y][x] = '0'
  num += 1

  to = to_move(y, x)
  if not to:
    return

  for new_y, new_x in to:
    dfs(new_y, new_x)
   
complex = []
for i in range(N):
  for j in range(N):
    if Map[j][i] == '1':
      num = 0
      dfs(j, i)
      complex.append(num)

complex.sort()
print(len(complex))
for i in complex:
  print(i)