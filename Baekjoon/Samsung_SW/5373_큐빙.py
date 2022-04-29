import sys
input = sys.stdin.readline

def rot_plane(plane, cw):
  if cw == '+':
    temp = plane[0][1]
    plane[0][1] = plane[1][0]
    plane[1][0] = plane[2][1]
    plane[2][1] = plane[1][2]
    plane[1][2] = temp

    temp = plane[0][0]
    plane[0][0] = plane[2][0]
    plane[2][0] = plane[2][2]
    plane[2][2] = plane[0][2]
    plane[0][2] = temp
    
  else:
    temp = plane[0][1]
    plane[0][1] = plane[1][2]
    plane[1][2] = plane[2][1]
    plane[2][1] = plane[1][0]
    plane[1][0] = temp

    temp = plane[0][0]
    plane[0][0] = plane[0][2]
    plane[0][2] = plane[2][2]
    plane[2][2] = plane[2][0]
    plane[2][0] = temp
  return

def F_rot_lines(cw):
  line_idx = [0, 2, 0, 0, 2]
  if cw == '+':
    temp = []
    for i in range(3):
      temp.append(left[i][line_idx[4]])
      
    for i in range(3):
      left[i][line_idx[4]] = bottom[line_idx[3]][i]
    for i in range(3):
      bottom[line_idx[3]][i] = right[-i-1][line_idx[2]]
    for i in range(3):
      right[i][line_idx[2]] = top[line_idx[1]][i]
    for i in range(3):
      top[line_idx[1]][i] = temp[-i-1]
  else:
    temp = []
    for i in range(3):
      temp.append(left[i][line_idx[4]])

    for i in range(3):
      left[i][line_idx[4]] = top[line_idx[1]][-i-1]
    for i in range(3):
      top[line_idx[1]][i] = right[i][line_idx[2]]
    for i in range(3):
      right[i][line_idx[2]] = bottom[line_idx[3]][-i-1]
    for i in range(3):
      bottom[line_idx[3]][i] = temp[i]
  return

def B_rot_lines(cw):
  # p1234 : 위, 오른쪽, 아래, 왼쪽
  line_idx = [0, 0, 0, 2, 2]

  if cw == '+':
    temp = []
    for i in range(3):
      temp.append(right[i][line_idx[4]])
    for i in range(3):
      right[i][line_idx[4]] = bottom[line_idx[3]][-i-1]
    for i in range(3):
      bottom[line_idx[3]][i] = left[i][line_idx[2]]
    for i in range(3):
      left[i][line_idx[2]] = top[line_idx[1]][-i-1]
    for i in range(3):
      top[line_idx[1]][i] = temp[i]
  else:
    temp = []
    for i in range(3):
      temp.append(right[i][line_idx[4]])

    for i in range(3):
      right[i][line_idx[4]] = top[line_idx[1]][i]
    for i in range(3):
      top[line_idx[1]][i] = left[-i-1][line_idx[2]]
    for i in range(3):
      left[i][line_idx[2]] = bottom[line_idx[3]][i]
    for i in range(3):
      bottom[line_idx[3]][i] = temp[-i-1]
  return

def R_rot_lines(cw):
  # p1234 : 위, 오른쪽, 아래, 왼쪽
  line_idx = [0, 2, 2, 2, 2]

  if cw == '+':
    temp = []
    for i in range(3):
      temp.append(front[i][line_idx[4]])
      
    for i in range(3):
      front[i][line_idx[4]] = bottom[i][line_idx[3]]
    for i in range(3):
      bottom[i][line_idx[3]] = back[-i-1][line_idx[2]]
    for i in range(3):
      back[i][line_idx[2]] = top[-i-1][line_idx[1]]
    for i in range(3):
      top[i][line_idx[1]] = temp[i]
  else:
    temp = []
    for i in range(3):
      temp.append(front[i][line_idx[4]])
      
    for i in range(3):
      front[i][line_idx[4]] = top[i][line_idx[1]]
    for i in range(3):
      top[i][line_idx[1]] = back[-i-1][line_idx[2]]
    for i in range(3):
      back[i][line_idx[2]] = bottom[-i-1][line_idx[3]]
    for i in range(3):
      bottom[i][line_idx[3]] = temp[i]
  return

def L_rot_lines(cw):
  # p1234 : 위, 오른쪽, 아래, 왼쪽
  line_idx = [0, 0, 0, 0, 0]

  if cw == '+':
    temp = []
    for i in range(3):
      temp.append(back[i][line_idx[4]])
      
    for i in range(3):
      back[i][line_idx[4]] = bottom[-i-1][line_idx[3]]
    for i in range(3):
      bottom[i][line_idx[3]] = front[i][line_idx[2]]
    for i in range(3):
      front[i][line_idx[2]] = top[i][line_idx[1]]
    for i in range(3):
      top[i][line_idx[1]] = temp[-i-1]
  else:
    temp = []
    for i in range(3):
      temp.append(back[i][line_idx[4]])
      
    for i in range(3):
      back[i][line_idx[4]] = top[-i-1][line_idx[1]]
    for i in range(3):
      top[i][line_idx[1]] = front[i][line_idx[2]]
    for i in range(3):
      front[i][line_idx[2]] = bottom[i][line_idx[3]]
    for i in range(3):
      bottom[i][line_idx[3]] = temp[-i-1]
  return

def U_rot_lines(cw):
  # p1234 : 위, 오른쪽, 아래, 왼쪽
  line_idx = [0, 0, 0, 0, 0]

  if cw == '+':
    temp = []
    for i in range(3):
      temp.append(left[line_idx[4]][i])
      
    for i in range(3):
      left[line_idx[4]][i] = front[line_idx[3]][i]
    for i in range(3):
      front[line_idx[3]][i] = right[line_idx[2]][i]
    for i in range(3):
      right[line_idx[2]][i] = back[line_idx[1]][-i-1]
    for i in range(3):
      back[line_idx[1]][i] = temp[-i-1]
  else:
    temp = []
    for i in range(3):
      temp.append(left[line_idx[4]][i])
      
    for i in range(3):
      left[line_idx[4]][i] = back[line_idx[1]][-i-1]
    for i in range(3):
      back[line_idx[1]][i] = right[line_idx[2]][-i-1]
    for i in range(3):
      right[line_idx[2]][i] = front[line_idx[3]][i]
    for i in range(3):
      front[line_idx[3]][i] = temp[i]
  return

def D_rot_lines(cw):
  # p1234 : 위, 오른쪽, 아래, 왼쪽
  line_idx = [0, 2, 2, 2, 2]

  if cw == '+':
    temp = []
    for i in range(3):
      temp.append(left[line_idx[4]][i])
      
    for i in range(3):
      left[line_idx[4]][i] = back[line_idx[3]][-i-1]
    for i in range(3):
      back[line_idx[3]][i] = right[line_idx[2]][-i-1]
    for i in range(3):
      right[line_idx[2]][i] = front[line_idx[1]][i]
    for i in range(3):
      front[line_idx[1]][i] = temp[i]
  else:
    temp = []
    for i in range(3):
      temp.append(left[line_idx[4]][i])
      
    for i in range(3):
      left[line_idx[4]][i] = front[line_idx[1]][i]
    for i in range(3):
      front[line_idx[1]][i] = right[line_idx[2]][i]
    for i in range(3):
      right[line_idx[2]][i] = back[line_idx[3]][-i-1]
    for i in range(3):
      back[line_idx[3]][i] = temp[-i-1]
  return
  
T = int(input())
for t in range(T):
  front = [['r']*3 for _ in range(3)]
  left = [['g']*3 for _ in range(3)]
  top = [['w']*3 for _ in range(3)]
  bottom = [['y']*3 for _ in range(3)]
  right = [['b']*3 for _ in range(3)]
  back = [['o']*3 for _ in range(3)]

  n = int(input())
  ops = list(input().split())
  
  for op in ops:
    plane = op[0]
    cw = op[1]
    if plane == 'U':
      rot_plane(top, cw)
      U_rot_lines(cw)
    if plane == 'D':
      rot_plane(bottom, cw)
      D_rot_lines(cw)
    if plane == 'F':
      rot_plane(front, cw)
      F_rot_lines(cw)
    if plane == 'B':
      B_rot_lines(cw)
      if cw == '+':
        cw = '-'
      else:
        cw = '+'
      rot_plane(back, cw)
    if plane == 'R':
      rot_plane(right, cw)
      R_rot_lines(cw)
    if plane == 'L':
      rot_plane(left, cw)
      L_rot_lines(cw)

  for row in top:
    for cell in row:
      print(cell, end='')
    print()