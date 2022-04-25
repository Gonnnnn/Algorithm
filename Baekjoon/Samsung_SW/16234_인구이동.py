import sys
from collections import deque
input = sys.stdin.readline

# map : N*N, L, R은 인구수 차이를 보는 기준
N, L, R = map(int, input().split())

Map = []
for _ in range(N):
  Map.append(list(map(int, input().split())))

def getUnion(visited, y, x):
  # 연합들을 모두 구해야한다. 구하면서 총 인구수, 국가 개수도 구해야한다. 해당 함수는 하나의 union을 구하는 함수이다.
  global N, L, R
  dy = [1, 0, -1, 0]
  dx = [0, 1, 0, -1]
  
  visited[y][x] = True
  # union에는 union에 해당하는 국가들의 idx를 넣는다
  union = [[y, x]]
  q = deque([[y, x, Map[y][x]]])
  count = 1
  totalNumOfPpl = Map[y][x]

  while(q):
    y, x, numOfPpl = q.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if 0 <= ny < N and 0 <= nx < N:
        tempNumOfPpl = Map[ny][nx]
        if L <= abs(tempNumOfPpl - numOfPpl) <= R and not visited[ny][nx]:
          # bfs를 위해 q에 추가
          q.append([ny, nx, Map[ny][nx]])
          
          union.append([ny, nx])
          count += 1
          totalNumOfPpl += tempNumOfPpl
          
          visited[ny][nx] = True

  if count == 1:
    return ([], 0)

  newPopulation = totalNumOfPpl // count

  return (union, newPopulation)

def simulate():
  global N
  day = 0

  while(True):
    visited = [[False]*N for _ in range(N)]
    unions = []
    newPops = []
    for i in range(N):
      for j in range(N):
        if not visited[i][j]:
          union, newPopulation = getUnion(visited, i, j)
          if union:
            unions.append(union)
            newPops.append(newPopulation)
    
    if not unions:
      return day

    day += 1
    for idx, union in enumerate(unions):
      newPop = newPops[idx]
      for y, x in union:
        Map[y][x] = newPop

  return -1
  
print(simulate())
