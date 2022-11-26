import sys
import copy

input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def willItSink(r, c, table):
    global dr, dc, R, C
    numOfSea = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 접하는 곳이 맵 밖이라면 => 바다라면
        if nr < 0 or R <= nr or nc < 0 or C <= nc:
            numOfSea += 1
            continue
        # 접하는 곳이 섬이라면
        if table[nr][nc] == 'X': continue
        # 접하는 곳이 맵 밖도 아니고, 섬도 아니라면 => 바다라면
        numOfSea += 1
    # 접하는 칸 중 3 혹은 4개의 칸이 바다라면
    if 3 <= numOfSea: return True
    return False


R, C = map(int, input().split(' '))
islands = []
table = []
for r in range(R):
    row = list(input().strip())
    table.append(row)
    for c in range(C):
        if row[c] == 'X':
            islands.append([r, c])

tableToRef = copy.deepcopy(table)
for r, c in islands:
    if willItSink(r, c, tableToRef):
        table[r][c] = '.'

minR = 0
maxR = R
minC = 0
maxC = C

for r in range(R):
    minR = r
    if 'X' in table[r]: break
for r in range(R - 1, -1, -1):
    maxR = r
    if 'X' in table[r]: break
for c in range(C):
    hasX = False
    minC = c
    for r in range(R):
        if table[r][c] == 'X':
            hasX = True
            break
    if hasX: break
for c in range(C - 1, -1, -1):
    hasX = False
    maxC = c
    for r in range(R):
        if table[r][c] == 'X':
            hasX = True
            break
    if hasX: break

for r in range(minR, maxR + 1):
    print(''.join(table[r][minC:maxC + 1]))
