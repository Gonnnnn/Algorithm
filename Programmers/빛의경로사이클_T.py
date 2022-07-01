def solution(grid):
    answer = []
    row = len(grid)
    col = len(grid[0])
    m = []
    for g in grid:
        m.append(list(g))
    visited = [[[0, 0, 0, 0] for _ in range(col)] for _ in range(row)]
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    for i in range(row):
        for j in range(col):
            for k in range(4):
                if visited[i][j][k] != 1:
                    cnt = 0
                    y, x, d = i, j, k
                    while(visited[y][x][d] != 1):
                        cnt += 1
                        visited[y][x][d] = 1
                        y, x = (y+dy[d])%row, (x+dx[d])%col
                        if m[y][x] == 'R':
                            d = (d-1+4)%4
                        elif m[y][x] == 'L':
                            d = (d+1)%4
                    answer.append(cnt)
    return sorted(answer)
