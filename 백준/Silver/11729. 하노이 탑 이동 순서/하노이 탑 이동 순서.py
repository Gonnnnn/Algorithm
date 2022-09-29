import sys
input = sys.stdin.readline
n = int(input().strip())

def solve(before, after, n):
    if n == 1:
        print(f'{before} {after}')
        return
    solve(before, 6-after-before, n-1)
    print(f'{before} {after}')
    solve(6-after-before, after, n-1)
    return
print((1<<n)-1)
solve(1, 3, n)