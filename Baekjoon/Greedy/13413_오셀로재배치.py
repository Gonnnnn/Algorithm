import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N = int(input())
  init = list(input().strip())
  goal = list(input().strip())

  init_black = 0
  goal_black = 0
  count = 0
  for i in range(N):
    if init[i] != goal[i]:
      count += 1    
      if init[i] == 'B':
        init_black += 1   
      if goal[i] == 'B':
        goal_black += 1

  dif = abs(init_black-goal_black)
  print(dif + (count-dif)//2)