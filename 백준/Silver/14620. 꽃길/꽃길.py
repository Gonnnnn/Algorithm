import sys
from itertools import combinations

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def getFiveCells(spot):
    y, x = spot // N, spot % N
    cells = [spot]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or N <= ny or nx < 0 or N <= nx:
            return [], False
        cells.append(ny * N + nx)
    return cells, True

def fillSet(cells, Set):
    for cell in cells:
        if cell in Set:
            return set(), False
        Set.add(cell)
    return Set, True

def getPrice(cells):
    price = 0
    for cell in cells:
        y, x = cell // N, cell % N
        price += table[y][x]
    return price

input = sys.stdin.readline
N = int(input())
table = [list(map(int, input().split(' '))) for _ in range(N)]
spots = [i for i in range(N*N)]

minPrice = float('inf')
for combination in combinations(spots, 3):
    Set = set()
    success = True
    for spot in combination:
        cells, ok = getFiveCells(spot)
        if not ok:
            success = False
            break
        Set, ok = fillSet(cells, Set)
        if not ok:
            success = False
            break
    if not success: continue
    minPrice = min(minPrice, getPrice(Set))

print(minPrice)