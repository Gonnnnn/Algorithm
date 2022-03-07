import copy
from collections import deque
from itertools import combinations

# 세로, 가로
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 2의 좌표들. [y, x]
twos = []
# 0의 좌표들. [y, x]
zeros = []
for i in range(N):
  for j in range(M):
    if Map[i][j] == 2:
      twos.append([i, j])
    if Map[i][j] == 0:
      zeros.append([i, j])

# 바이러스가 퍼져나갈 수 있는 좌표를 반환
def move(y, x):
  global N, M
  dy = [1, 0, -1, 0]
  dx = [0, 1, 0, -1]

  to = []
  for i in range(4):
    new_y = y + dy[i]
    new_x = x + dx[i]
    if 0<=new_y<N and 0<=new_x<M:
      if temp_Map[new_y][new_x] == 0:
        to.append([new_y, new_x])
  return to

# 바이러스 확산 방식을 보면 BFS. 하나의 지점으로부터 같은 step 내에 있는 곳부터 퍼져나감
def BFS(y, x):
  q = deque([[y, x]])
  while(q):
    y1, x1 = q.popleft()
    if temp_Map[y1][x1] == 1:
      continue
    # 바이러스에 감염된 곳은 어차피 더 이상 바이러스가 확산해 나갈 수 있는 지점인지 확인할 필요가 없다.
    # 따라서 벽과 같은 취급을 해주기 위해 1로 바꾼다
    # 또한 이러한 방법은 추후에 N*M에서 temp_Map 전체 값을 빼줌으로써 값이 0인 지점의 개수를 세는데 용이하다.
    temp_Map[y1][x1] = 1
    to = move(y1, x1)
    for y2, x2 in to:
      q.append([y2, x2])    
  return

result = 0
for case in combinations(zeros, 3):
  # Map 복사
  temp_Map = copy.deepcopy(Map)
  # 벽 세우기
  for y, x in case:
    temp_Map[y][x] = 1
  # 바이러스가 있는 곳을 기준으로 BFS
  for y, x in twos:
    BFS(y, x)
  
  Sum = 0
  for row in temp_Map:
    Sum += sum(row)

  result = max(result, N*M-Sum)

print(result)


# 벽을 세우는 모든 경우를 확인하기 위해 그 때 그 때 Map을 복사
# 단순 무식한데 나쁘지 않은 방법이었다. 처음에는 DFS를 썼다.
# result = 0
# for i in range(N*M-2):
#   y1, x1 = i//M, i%M
#   if Map[y1][x1] == 0:
#     for j in range(i+1, N*M-1):
#       y2, x2 = j//M, j%M
#       if Map[y2][x2] == 0:
#         for k in range(j+1, N*M):
#           y3, x3 = k//M, k%M
#           if Map[y3][x3] == 0:
#             temp_Map = copy.deepcopy(Map)
#             temp_Map[y1][x1] = 1
#             temp_Map[y2][x2] = 1
#             temp_Map[y3][x3] = 1
#             for y, x in twos:
#               DFS(y, x)
#             Sum = 0
#             for row in temp_Map:
#               Sum += sum(row)
#             result = max(result, N*M-Sum)

# print(result)