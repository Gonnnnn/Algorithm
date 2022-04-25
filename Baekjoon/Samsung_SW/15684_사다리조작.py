# M개의 가로선, N개의 세로선
# 세로선마다 H개의 가로선을 놓을 수 있음

# i번 세로선의 결과가 i번이 되게 하는 최소 가로선 개수
import copy

N, M, H = map(int, input())

Map = [[0]*(N+1) for _ in range(H+1)]
# Map[i][j] == 1 -> j번째 줄에서, i, i+1번째 세로선을 잇는다.

# 오른쪽으로 이어지면 1 왼쪽으로 이어지면 -1
for _ in range(M):
  a, b = map(int, input())
  Map[a][b] = 1
  Map[a][b+1] = -1

def simulate(tempMap):
  global N, H
  match = True
  for j in range(1, N+1):
    x = j
    y = 1
    while(True):
      if y == H + 1:
        break
      if tempMap[y][x] == 1:
        x += 1
      elif tempMap[y][x] == -1:
        x -= 1
      y += 1

    if x != j:
      match = False
      break

  return match

# BFS? 조건 중에 가로선이 이어지는 경우들은 배제해야할 것이고, simulate를 매 BFS마다 돌려야할 것, 또한 더이상 가로 선을 추가할 수 없는 경우를 base case로 해야할 것, 몇번째 layer인지 count해야할 것이고, 성공하면 바로 break 

def findLines(tempMap):
  # tempMap 기준으로 추가 가능한 line들을 찾아야한다.
  # spots에는 추가 가능한 line이 담긴다. 해당 line의 idx는 시작점이며, 왼쪽에서 오른쪽으로 이어지는 line이다.
  spots = []
  for i in range(1, H+1):
    for j in range(1, N):
      if tempMap[i][j] != 0:
        continue
      else:
        spots.append([i, j])        
        
  return spots
  
def bfs(count, map):
  global M, N, H

  spots = findLines(map)
  if not spots:
    return count

  for y, x in spots:
    tempMap = copy.deepcopy(map)
    tempMap[y][x] = 1
    tempMap[y][x+1] = -1

    result = simulate(tempMap)
    if result:
      return count

  return

