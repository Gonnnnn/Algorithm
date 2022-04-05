class token:
  def __init__(self, r, c, dir, num):
    self.r = r
    self.c = c
    self.dir = dir
    self.prev = None
    self.next = None
    self.num = num

  def __repr__(self):
    return f'token{self.num}'

N, K = map(int, input().split())
# 0 : w, 1 : r, 2 : b
board = [list(map(int, input().split())) for _ in range(N)]
token_map = [[None]*N for _ in range(N)]
count_map = [[0]*N for _ in range(N)]
tokens = {}
for k in range(K):
  # dir 1 : r, 2 : l, 3 : u, 4 : d
  r, c, dir = map(int, input().split())
  tokens[k] = token(r-1, c-1, dir, k)
  token_map[r-1][c-1] = tokens[k]
  count_map[r-1][c-1] += 1

def move(board, token_map, count_map, token, turn):
  global N
  dr = [0, 0, 0, -1, 1]
  dc = [0, 1, -1, 0, 0]
  nr, nc = token.r + dr[token.dir], token.c + dc[token.dir]
  if 0 <= nr < N and 0 <= nc < N:
    cell = board[nr][nc]
    if cell == 0:
      token_map[token.r][token.c] = token.prev
      if token.prev != None:
        token.prev.next = None
      temp = token
      last = None
      while(temp != None):
        count_map[temp.r][temp.c] -= 1
        
        temp.r, temp.c = nr, nc
        if temp.next == None:
          last = temp
        count_map[nr][nc] += 1
        
        temp = temp.next

      token.prev = token_map[nr][nc]
      if token_map[nr][nc] != None:
        token_map[nr][nc].next = token
      token_map[nr][nc] = last
      
    elif cell == 1:
      token_map[token.r][token.c] = token.prev
      new_first_prev = token.prev
      if token.prev != None:
        token.prev.next = None
      temp = token
      new_last = token
      new_first = None
      while(temp != None):
        count_map[temp.r][temp.c] -= 1
        temp.r, temp.c = nr, nc
        temp_prev = temp.prev
        temp_next = temp.next
        
        temp.prev = temp_next
        temp.next = temp_prev
 
        count_map[nr][nc] += 1
        if temp_next == None:
          new_first = temp
        temp = temp_next
      
      new_last.next = None
      new_first.prev = new_first_prev
      token = new_first
      
      token.prev = token_map[nr][nc]  
      if token_map[nr][nc] != None:
        token_map[nr][nc].next = token
      token_map[nr][nc] = new_last
    else:
      if turn == 0:
        if token.dir == 1:
          token.dir = 2
        elif token.dir == 2:
          token.dir = 1
        elif token.dir == 3:
          token.dir = 4
        else:
          token.dir = 3
        move(board, token_map, count_map, token, turn + 1)
  else:
    if turn == 0:
      if token.dir == 1:
        token.dir = 2
      elif token.dir == 2:
        token.dir = 1
      elif token.dir == 3:
        token.dir = 4
      else:
        token.dir = 3
      move(board, token_map, count_map, token, turn + 1)
        
  return

count = 0
while(count <= 1000):
  Break = False
  for row in count_map:
    if 4 in row:
      Break = True
      break
  if Break:
    break
  for row in count_map:
    print(row)
  for k in range(K):
    token = tokens[k]
    move(board, token_map, count_map, token, 0)
    for p in range(K):
      print(f'token{tokens[p].num} : next={tokens[p].next}, prev={tokens[p].prev}, r={tokens[p].r}, c={tokens[p].c}')
    print('--------------------------')
  for row in count_map:
    print(row)

  count += 1
  print(count)

if count > 1000:
  count = -1
print(count)