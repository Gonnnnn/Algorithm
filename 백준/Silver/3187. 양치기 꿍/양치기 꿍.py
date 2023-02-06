import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split(' '))
farm = [list(input().strip()) for _ in range(R)]
EMPTY, FENCE, WOLF, SHEEP = '.', '#', 'v', 'k'
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def solve(y, x):
    animalCounter = {SHEEP: 0, WOLF: 0}
    q = deque([(y, x)])
    cell = farm[y][x]
    if cell == SHEEP or cell == WOLF:
        animalCounter[cell] += 1
    farm[y][x] = FENCE

    while(q):
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or R <= ny or nx < 0 or C <= nx: continue
            if farm[ny][nx] == FENCE: continue
            q.append((ny, nx))
            if not farm[ny][nx] == EMPTY:
                animalCounter[farm[ny][nx]] += 1
            farm[ny][nx] = FENCE
    return animalCounter[SHEEP], animalCounter[WOLF]

survivedSheepNumber, survivedWolfNumber = 0, 0
for i in range(R):
    for j in range(C):
        if farm[i][j] == FENCE: continue
        sheepNumber, wolfNumber = solve(i, j)
        if sheepNumber > wolfNumber: survivedSheepNumber += sheepNumber
        else: survivedWolfNumber += wolfNumber
print(survivedSheepNumber, survivedWolfNumber)