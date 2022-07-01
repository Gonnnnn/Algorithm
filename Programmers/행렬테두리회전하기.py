def solution(rows, columns, queries):
    answer = []
    t = []
    for i in range(rows):
        t.append(list(range(i*columns + 1, (i+1)*columns+1)))
    for q in queries:
        # x:행, y:열
        answer.append(rotate(t, q))
    return answer

def rotate(t, q):
    x1 = q[0] - 1
    y1 = q[1] - 1
    x2 = q[2] - 1
    y2 = q[3] - 1
    temp = t[x1][y1]
    Min = temp
    for i in range(x1, x2):
        t[i][y1] = t[i+1][y1]
        if t[i][y1] < Min:
            Min = t[i][y1]
    for j in range(y1, y2):
        t[x2][j] = t[x2][j+1]
        if t[x2][j] < Min:
            Min = t[x2][j]
    for i in range(x2, x1, -1):
        t[i][y2] = t[i-1][y2]
        if t[i][y2] < Min:
            Min = t[i][y2]
    for j in range(y2, y1, -1):
        t[x1][j] = t[x1][j-1]
        if t[x1][j] < Min:
            Min = t[x1][j]
    t[x1][y1+1] = temp
    return Min