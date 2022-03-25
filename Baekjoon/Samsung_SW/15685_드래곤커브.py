N = int(input())

# x,y 시작점 d 방향, g 세대
# d : 0 오른, 1 위, 2 왼, 3 아래
curves = [list(map(int, input().split())) for _ in range(N)]

Map = [[0]*101 for _ in range(101)]

def dragon(y, x, d, g):
  dy = [0, -1, 0, 1]
  dx = [1, 0, -1, 0]
  Map[y][x] = 1
  ny = y+dy[d]
  nx = x+dx[d]
  Map[ny][nx] = 1
  curve = [[y, x], [ny, nx]]
    
  while(g > 0):
    y = curve[-1][0]
    x = curve[-1][1]
    # 새로운 curve의 끝점은 현재 curve의 시작점이 회전이동한 결과일 것이므로, curve의 끝 부분부터 mapping을 시작한다
    curve_len = len(curve)
    temp = []
    for i in range(curve_len - 1, -1, -1):
      cy = curve[i][0]
      cx = curve[i][1]
      # 끝점에 대해 회전 = 끝점을 원점으로 좌표 변환(translation), 회전(rotation) 후 다시 좌표 복원(translation)
      # translation
      ty = cy-y
      tx = cx-x
      # rotation + translation
      ny = tx + y
      nx = -ty + x
      # 지도에 표기
      Map[ny][nx] = 1
      temp.append([ny, nx])
    curve += temp
    g -= 1
  return

def check(y, x):
  to_check = [[y, x], [y, x+1], [y+1, x], [y+1, x+1]]
  for ty, tx in to_check:
    if 0 <= ty < 101 and 0 <= tx < 101:
      if Map[ty][tx] == 0:
        return 0
    else:
      return 0
  return 1

for x, y, d, g in curves:
  dragon(y, x, d, g)

result = 0
for i in range(100):
  for j in range(100):
    result += check(i, j)
print(result)