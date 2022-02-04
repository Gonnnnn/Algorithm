# 문제
# N×M크기의 배열로 표현되는 미로가 있다.

# 1	0	1	1	1	1
# 1	0	1	0	1	0
# 1	0	1	0	1	1
# 1	1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

# 00

import sys
import heapq as hq
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(N)]
INF = N*M

dx = [1, -1]
dy = [1, -1]

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
# 이런식으로 해서 for문 돌리는 방법도 있다.

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