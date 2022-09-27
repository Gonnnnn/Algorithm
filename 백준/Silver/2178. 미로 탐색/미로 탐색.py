import sys
import heapq as hq
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(N)]
INF = N*M

dx = [1, -1]
dy = [1, -1]

def check_adjacent(y, x):
  adjacent_ones = []

  for i in dy:
    if(y+i < 0 or y+i >= N):
      continue
    if(maze[y+i][x]):
      adjacent_ones.append([y+i, x]) 

  for j in dx:
    if(x+j < 0 or x+j >= M):
      continue
    if(maze[y][x+j]):
      adjacent_ones.append([y, x+j]) 

  return adjacent_ones

d = [[INF for _ in range(M)] for _ in range(N)]

def Daoohoo(y, x):
  d[0][0] = 1
  q = []
  hq.heappush(q, (d[y][x], y, x))

  while q:
    dist, cur_y, cur_x = hq.heappop(q)
    if dist > d[cur_y][cur_x]:
      continue

    adjacents = check_adjacent(cur_y, cur_x)

    for node in adjacents:
      new_dist = dist + 1
      if new_dist < d[node[0]][node[1]]:
        d[node[0]][node[1]] = new_dist
        hq.heappush(q, (new_dist, node[0], node[1]))


Daoohoo(0, 0)
print(d[N-1][M-1])