from collections import deque

N = int(input())
Map = []
shark_pos = []
shark_size = 2
for i in range(N):
  row = list(map(int, input().split()))
  Map.append(row)
  if 9 in row:
    shark_pos = [i, row.index(9)]

def find_fish(y, x):
  global N, shark_pos, shark_size
  dy = [-1, 0, 0, 1]
  dx = [0, -1, 1, 0]
  visited = [[False]*N for _ in range(N)]
  visited[y][x] = True
  q = deque([[y, x]])

  sec = 0
  fish = []
  stop = False
  while(q and not stop):
    itr = len(q)
    sec += 1
    for _ in range(itr):
      y, x = q.popleft()
      for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
          fish_size = Map[ny][nx]
          if not visited[ny][nx] and fish_size <= shark_size:
            if 0 < fish_size < shark_size:
              stop = True
              fish.append([ny, nx])
            else:
              visited[ny][nx] = True
              q.append([ny, nx])

  if not fish:
    return fish
  
  cy, cx = fish[0]
  for y, x in fish:
    if y < cy:
      cy = y
      cx = x
  for y, x in fish:
    if y == cy and x < cx:
      cx = x

  return [cy, cx, sec]

time = 0
count = 0
while(True):
  y, x = shark_pos
  fish = find_fish(y, x)
  
  if not fish:
    print(time)
    break

  Map[shark_pos[0]][shark_pos[1]] = 0
  shark_pos = [fish[0], fish[1]]
  Map[fish[0]][fish[1]] = 9

  count += 1
  if count == shark_size:
    shark_size += 1
    count = 0
  time += fish[2]