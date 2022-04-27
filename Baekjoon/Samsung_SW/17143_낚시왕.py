import sys
input = sys.stdin.readline

class shark:
  def __init__(self, y, x, speed, direction, size, number):
    self.y = y
    self.x = x
    self.speed = speed
    self.direction = direction
    self.size = size
    self.number = number
  def __repr__(self):
    return f'shark{self.number}'

def move(sharks):
  global R, C
  dy = [0, -1, 1, 0, 0]
  dx = [0, 0, 0, 1, -1]

  temp_Map = [[None]*(C+1) for _ in range(R+1)]
  sharks_to_kill = []
  
  for idx in sharks:
    shark = sharks[idx]
    # shark moves
    y, x, s, d = shark.y, shark.x, shark.speed, shark.direction 

    while(s > 0):
      ny = y + dy[d]
      nx = x + dx[d]
      if 1 <= ny < R+1 and 1 <= nx < C+1:
        y = ny
        x = nx
        s -= 1
      else:
        if d == 1:
          d = 2
        elif d == 2:
          d = 1
        elif d == 3:
          d = 4
        else:
          d = 3
          
    shark.y, shark.x, shark.direction = y, x, d

    if temp_Map[y][x] != None:
      another_shark = temp_Map[y][x]
      if another_shark.size < shark.size:
        sharks_to_kill.append(another_shark.number)
        temp_Map[y][x] = shark
      else:
        sharks_to_kill.append(shark.number)
    else:
      temp_Map[y][x] = shark

  for idx in sharks_to_kill:
    del sharks[idx]

  return temp_Map, sharks

R, C, M = map(int, input().split())
Map = [[None]*(C+1) for _ in range(R+1)]
sharks = {}

for i in range(M):
  r, c, s, d, z = map(int, input().split())
  temp = shark(r, c, s, d, z, i+1)
  Map[r][c] = temp
  sharks[i+1] = temp

result = 0
for j in range(1, C+1):
  # catch the closest shark 
  for i in range(1, R+1):
    if Map[i][j] != None:
      shark = Map[i][j]
      result += shark.size
      Map[i][j] = None
      del sharks[shark.number]
      break
  
  Map, sharks = move(sharks)
  
print(result)