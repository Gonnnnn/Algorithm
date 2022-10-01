import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split(' '))
visited = [False for _ in range(n + 1)]
def solve(num, nums):
    global n, m
    if len(nums) == m:
        print(' '.join(map(str, nums)))
        return
    for i in range(1, n + 1):
        if visited[i]: continue
        nums.append(i)
        visited[i] = True
        solve(i, nums)
        visited[i] = False
        nums.pop()
    return
solve(0, [])