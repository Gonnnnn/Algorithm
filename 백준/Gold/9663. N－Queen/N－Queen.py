import sys
input = sys.stdin.readline
n = int(input().strip())
col = [False for _ in range(n)]
diagonal1 = [False for _ in range(2 * n - 1)]
diagonal2 = [False for _ in range(2 * n - 1)]
cnt = 0

def solve(row):
    global cnt, n
    if row == n:
        cnt += 1
        return

    for i in range(n):
        if col[i] or diagonal1[row + i] or diagonal2[n - 1 - i + row]: continue
        col[i] = True
        diagonal1[row + i] = True
        diagonal2[n - 1 - i + row] = True
        solve(row + 1)
        col[i] = False
        diagonal1[row + i] = False
        diagonal2[n - 1 - i + row] = False
    return
solve(0)
print(cnt)