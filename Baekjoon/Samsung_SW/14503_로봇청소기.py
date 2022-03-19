import sys
input = sys.stdin.readline

# 세로, 가로
N, M = map(int, input().split())
# d = north, east, south, west
y, x, d = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
before = 0
for i in range(N):
    for j in range(M):
        before += Map[i][j]

# 청소할 곳이 있는지 규칙에 따라 왼쪽으로 돌며 확인해주는 함수
# 없다면 후진한 후의 좌표를 반환한다.
# 후진도 불가능하다면 빈 리스트를 반환한다.
def check(y, x, d):
    global N, M
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    temp = []
    for i in range(1, 5):
        idx = d - i
        ny = y + direction[idx][0]
        nx = x + direction[idx][1]
        if 0 <= ny < N and 0 <= nx < M:
            if Map[ny][nx] == 0:
                temp = [ny, nx, (idx + 4) % 4]
                break

    if not temp:
        if Map[y - direction[d][0]][x - direction[d][1]] != 1:
            temp = [y - direction[d][0], x - direction[d][1], d]

    return temp

def solve(y, x, d):
    while(True):
        Map[y][x] = -1
        to = check(y, x, d)
        if not to:
            break
        y = to[0]
        x = to[1]
        d = to[2]
    return

solve(y, x, d)

after = 0
for i in range(N):
    for j in range(M):
        after += Map[i][j]

print(before - after)