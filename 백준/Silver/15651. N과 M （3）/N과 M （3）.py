import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split(' '))

def solve(nums):
    global n, m
    if len(nums) == m:
        print(' '.join(list(map(str, nums))))
        return
    for i in range(1, n+1):
        nums.append(i)
        solve(nums)
        nums.pop()
    return

solve([])