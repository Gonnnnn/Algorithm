import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split(' '))
randNums = list(map(int, input().strip().split(' ')))
randNums.sort()

def solve(nums, start):
    global n
    if len(nums) == m:
        print(' '.join(list(map(str, nums))))
        return
    temp = 0
    for i in range(start, n):
        if temp == randNums[i]: continue
        temp = randNums[i]
        nums.append(randNums[i])
        solve(nums, i)
        nums.pop()
    return
solve([], 0)