import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
Map = [[0]*(N+1) for _ in range(N+1)]
K = int(input())
# apples = [list(map(int, input().split())) for _ in range(K)]
for _ in range(K):
  y, x = map(int, input().split())
  Map[y][x] = 1
L = int(input())
curves = []
for _ in range(L):
  sec, direction = input().split()
  curves.append([int(sec), direction])
  
def solve(y, x):
  global N, L

  snake = deque()
  snake.append([1, 1])

  dy = [-1, 0, 1, 0]
  dx = [0, 1, 0, -1]
  move_idx = 1
  time = 0
  curve_idx = 0
  
  while(True):
    time += 1
    ny = snake[0][0] + dy[move_idx]
    nx = snake[0][1] + dx[move_idx]
    
    if (ny < 1 or ny > N or nx < 1 or nx > N) or [ny, nx] in snake:
      break

    snake.appendleft([ny, nx])
    if Map[ny][nx]:
      Map[ny][nx] = 0
    else:
      snake.pop()

    if curve_idx < L and time == curves[curve_idx][0]:
      if curves[curve_idx][1] == 'D':
        move_idx = (move_idx + 1) % 4
      else:
        move_idx = (move_idx - 1) % 4
      curve_idx += 1

  return time

print(solve(1, 1))