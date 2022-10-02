import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split(' '))

def solve(start, nums):
    global n, m
    if len(nums) == m:
        print(' '.join(list(map(str, nums))))
        return
    for i in range(start, n+1):
        nums.append(i)
        solve(i + 1, nums)
        nums.pop()
    return

solve(1, [])