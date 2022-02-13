import copy

class Fish:
  def __init__(self, order, direction, location):
    self.order = order
    self.direction = direction
    self.location = location
    self.fish = True
  
def fish_move(one, Map, fish_li):
  dxdy = [[-1, 0],[-1, -1], [0, -1], [1, -1],
      [1, 0], [1, 1], [0, 1], [-1, 1]]

  for i in range(0, len(dxdy)):
    location_x = one.location[0] + dxdy[(one.direction-1+i)%8][0]
    location_y = one.location[1] + dxdy[(one.direction-1+i)%8][1]

    # 맵을 벗어나면 이동하지 못한다
    if location_x >= 4 or location_x < 0 or location_y >= 4 or location_y < 0:
      continue
    else:
      # cell이 비어있으면 거기로 바로 이동한다. 다른 물고기의 location을 갱신할 필요가 없다.
      if Map[location_x][location_y] == None:
        one.direction = (one.direction-1+i)%8 + 1

        Map[location_x][location_y] = one.order
        Map[one.location[0]][one.location[1]] = None
        one.location = [location_x, location_y]
        break
      # 비어있지 않다면 물고기 혹은 상어가 있다.
      else:
        # 상어가 있는 경우, 이동하지 못하므로 넘어간다.
        if not fish_li[Map[location_x][location_y]].fish:
          continue
        # 물고기가 있으니 Map상에서 물고기를 교환해주고, 물고기 자체의 정보도 update해준다
        else:
          other_fish = fish_li[Map[location_x][location_y]]
          # Map상에서 물고기 위치를 교환해준다
          Map[location_x][location_y] = one.order
          Map[one.location[0]][one.location[1]] = other_fish.order

          # 물고기들의 정보를 update해준다
          other_fish.location = [one.location[0], one.location[1]]
          one.location[0] = location_x
          one.location[1] = location_y
          one.direction = (one.direction-1+i)%8 + 1
          break


class Shark:
  def __init__(self, have_eaten, direction, location):
    self.order = 0
    self.have_eaten = have_eaten
    self.direction = direction
    self.location = location
    self.fish = False
  
  def point_to_move_to(self, count):
    dxdy = [[-1, 0],[-1, -1], [0, -1], [1, -1],
        [1, 0], [1, 1], [0, 1], [-1, 1]]
    location_x = self.location[0] + dxdy[self.direction-1][0] * count
    location_y = self.location[1] + dxdy[self.direction-1][1] * count
    
    return [location_x, location_y]
    

def shark_scan(one, Map):
  dxdy = [[-1, 0],[-1, -1], [0, -1], [1, -1],
      [1, 0], [1, 1], [0, 1], [-1, 1]]
  count = 0
  possible_cells = []
  location_x = one.location[0]
  location_y = one.location[1]
  while(True):
    location_x += dxdy[one.direction-1][0]
    location_y += dxdy[one.direction-1][1]
    count += 1

    if location_x >= 4 or location_x < 0 or location_y >= 4 or location_y < 0:
      break
    elif Map[location_x][location_y] == None:
      continue
    else:
      possible_cells.append(count)

  return possible_cells


def shark_eat(one, Map, fish_li, what_to_eat):
  fish_to_eat = fish_li[Map[what_to_eat[0]][what_to_eat[1]]]
  fish_li[fish_to_eat.order] = None
  
  one.have_eaten += fish_to_eat.order
  one.direction = fish_to_eat.direction
  Map[one.location[0]][one.location[1]] = None
  one.location = fish_to_eat.location

  Map[what_to_eat[0]][what_to_eat[1]] = one.order


fish_li = [0]*17
Map = [[None, None, None, None] for _ in range(4)]
for i in range(4):
  temp = list(map(int, input().split()))
  for j in range(0, 7, 2):
    fish_li[temp[j]] = Fish(temp[j], temp[j+1], [i, j//2])
    Map[i][j//2] = temp[j]

first_fish = fish_li[Map[0][0]]
shark = Shark(first_fish.order, first_fish.direction, first_fish.location)
fish_li[0] = shark
fish_li[first_fish.order] = None
Map[0][0] = shark.order

answer = 0
def go(Map, fish_li, shark, result, order):
  global answer

  Map_save = copy.deepcopy(Map)
  fish_li_save = copy.deepcopy(fish_li)
  for i in range(1,len(fish_li_save)):
    one = fish_li_save[i]
    if one != None:
      fish_move(one, Map_save, fish_li_save)


  possible_cells = shark_scan(shark, Map_save)
  if len(possible_cells) == 0:
    answer = max(result, answer)
    return
  

  for i in possible_cells:
    new_shark = copy.deepcopy(shark)
    Map_to_hand_to_next = copy.deepcopy(Map_save)
    fish_li_to_hand_to_next = copy.deepcopy(fish_li_save)
    new_location = new_shark.point_to_move_to(i)
    shark_eat(new_shark, Map_to_hand_to_next, fish_li_to_hand_to_next, new_location)

    go(Map_to_hand_to_next, fish_li_to_hand_to_next, new_shark, new_shark.have_eaten, order+1)

  
go(Map, fish_li, shark, shark.have_eaten, 1)

print(answer)

  


# 상어가 갈 수 있는 곳의 선택지들을 확인
# 각각의 선택지를 먹었을 때 물고기들이 재배치되는 결과는 다를 것


# 아래와 같은 경우는 상어가 집에 돌아가야하는 경우읻.
# 일단 상어가 택한 물고기의 방향이 맵 밖을 향하는 경우. 잡아먹고 집을 가야한다.
# 선택하고 물고기를 재배치해 봤을 때, 먹을 수 있는 물고기가 없는 경우

# 위와 같은 경우가 아니라면, 상어가 집에 가야할 경우마다 기존의 경우의 값과 비교하여 큰 값을 택하는 식으로 비교해준다.

# 기존의 경우로 돌아가야하는 경우는 다음과 같이 처리한다.
# 매 경우의 Map정보를 stack으로 쌓는 것이다. 이 때, 잡아먹을 수 있는 물고기의 경우의 수도 함께 저장해야할 것이다. 무엇을 먹었는지 알기 위해서. 이는 DFS로해결될 것

