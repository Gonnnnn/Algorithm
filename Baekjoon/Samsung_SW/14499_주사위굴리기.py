# 가로, 세로, 주사위x, 주사위y, 명령 개수
N, M, x, y, K = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))

def new_xy(x, y, idx):
  global N, M
  dx = [0, 0, 0, -1, 1]
  dy = [0, 1, -1, 0, 0]

  nx = x + dx[idx]
  ny = y + dy[idx]

  if 0 <= nx < N and 0 <= ny < M:
    return [nx, ny]

  return [-1, -1]

def roll(idx):
  # 동, 서, 남, 북 == 1, 2, 3, 4
  if idx == 1:
    # 1->3 3->6 6->4 4->1
    dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
  elif idx == 2:
    # 1->4 4->6 6->3 3->1
    dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
  elif idx == 3:
    # 1->2 2->6 6->5 5->1
    dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
  elif idx == 4:
    # 1->5 5->6 6->2 2->1
    dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
  return

dice = [0, 0, 0, 0, 0, 0, 0]
for i in moves:
  nx, ny = new_xy(x, y, i)
  if ny == -1:
    continue
  x, y = nx, ny
  roll(i)
  if Map[x][y] == 0:
    Map[x][y] = dice[6]
  else:
    dice[6] = Map[x][y]
    Map[x][y] = 0
  print(dice[1])