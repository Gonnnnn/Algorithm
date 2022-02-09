# 문제
# 상근이는 우리나라에서 가장 유명한 놀이 공원을 운영하고 있다. 이 놀이 공원은 야외에 있고, 다양한 롤러코스터가 많이 있다.

# 어느 날 벤치에 앉아있던 상근이는 커다란 황금을 발견한 기분이 들었다. 자신의 눈 앞에 보이는 이 부지를 구매해서 롤러코스터를 만든다면, 세상에서 가장 재미있는 롤러코스터를 만들 수 있다고 생각했다.

# 이 부지는 직사각형 모양이고, 상근이는 R행 C열의 표 모양으로 나누었다. 롤러코스터는 가장 왼쪽 위 칸에서 시작할 것이고, 가장 오른쪽 아래 칸에서 도착할 것이다. 롤러코스터는 현재 있는 칸과 위, 아래, 왼쪽, 오른쪽으로 인접한 칸으로 이동할 수 있다. 각 칸은 한 번 방문할 수 있고, 방문하지 않은 칸이 있어도 된다.

# 각 칸에는 그 칸을 지나갈 때, 탑승자가 얻을 수 있는 기쁨을 나타낸 숫자가 적혀있다. 롤러코스터를 탄 사람이 얻을 수 있는 기쁨은 지나간 칸의 기쁨의 합이다. 가장 큰 기쁨을 주는 롤러코스터는 어떻게 움직여야 하는지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 R과 C가 주어진다. (2 ≤ R, C ≤ 1000) 둘째 줄부터 R개 줄에는 각 칸을 지나갈 때 얻을 수 있는 기쁨이 주어진다. 이 값은 1000보다 작은 양의 정수이다.

# 출력
# 첫째 줄에 가장 가장 큰 기쁨을 주는 롤러코스터는 가장 왼쪽 위 칸부터 가장 오른쪽 아래 칸으로 어떻게 움직이면 되는지를 출력한다. 위는 U, 오른쪽은 R, 왼쪽은 L, 아래는 D로 출력한다. 정답은 여러 가지 일 수도 있다.

# 생각 더해야겠네. 현재 코드로는 두개의 케이스를 놓친다. 케이스를 정확히 알고있기에 하면 될거같긴한데, 더 깔끔히 제대로 열심히 해보고 싶다. 그냥 싹 지우고 나중에 다시 시도해봐도될듯 ㅎㅎ

R, C = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(R)]

result = ''
if R % 2 == 1:
  while(R != 0):
    if(R % 2 == 1):
      result += 'R' * (C-1)
    else:
      result += 'L' * (C-1)
    R -= 1
    if R != 0:
      result += 'D'

elif C % 2 == 1:
  while(C != 0):
    if(C % 2 == 1):
      result += 'D' * (R-1)
    else:
      result += 'U' * (R-1)
    C -= 1
    if C != 0:
      result += 'R'
  
else:
  def navigate(result, row, col):
    global R, C
    cur_row = 0
    while(R != cur_row):

      if cur_row//2 < row//2:
        if(cur_row % 2 == 0):
          result += 'R' * (C-1)
        else:
          result += 'L' * (C-1)
      elif cur_row//2 == row//2:
        down = True
        for i in range(C-1):
          if i < col:
            if down:
              result += 'DR'
              down = False
            else:
              result += 'UR'
              down = True
          else:
            if down:
              result += 'RD'
              down = False
            else:
              result += 'RU'
              down = True
        cur_row += 1
      else:
        if(cur_row % 2 == 0):
          result += 'L' * (C-1)
        else:
          result += 'R' * (C-1)

        
      cur_row += 1
      if cur_row != R:
        result += 'D'

    return result

  Max_limit = 1000

  # 첫번째, 마지막 값은 무조건 지나야 하므로 아래 for문에서 걸러지면 안됨
  first_value = Map[0][0]
  last_value = Map[R-1][C-1]
  Map[0][0] = Max_limit
  Map[R-1][C-1] = Max_limit

  # (value, row, column)
  Min = (Max_limit, 0, 0)
  for i, row in enumerate(Map):
    for j in range(1, len(row), 2):
      if Min[0] > row[j]:
        Min = (row[j], i, j) 
  Map[0][0] = first_value
  Map[R-1][C-1] = last_value

  result = navigate(result, Min[1], Min[2])

print(result)

# 2 2 2 2 2 2
# 2 2 2 2 2 2
# 2 2 1 2 2 2
# 2 2 2 2 2 2
# 2 2 2 2 2 2
# 2 2 2 2 2 2
