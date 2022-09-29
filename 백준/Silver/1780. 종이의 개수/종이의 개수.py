import sys
import math
input = sys.stdin.readline
n = int(input().strip())
paper = [list(map(int, input().strip().split(' '))) for _ in range(n)]
k = 0
while(n != 1):
    n = n // 3
    k += 1

def solve(k, r, c):
    result = [0, 0, 0]
    if k == 0:
        result[paper[r][c] + 1] += 1
        return result

    toAdd = int(math.pow(3, k-1))
    for i in range(3):
        nr = r + toAdd * i
        for j in range(3):
            nc = c + toAdd * j
            subResult = solve(k-1, nr, nc)
            for p in range(3):
                result[p] += subResult[p]
    Sum = sum(result)
    for i, re in enumerate(result):
        if re == Sum:
            result[i] = 1
            return result
    return result

result = solve(k, 0, 0)
for r in result:
    print(r)