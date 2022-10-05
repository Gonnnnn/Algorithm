import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split(' '))
randNums = list(map(int, input().strip().split(' ')))
randNums.sort()

def solve(nums):
    global n
    if len(nums) == m:
        print(' '.join(list(map(str, nums))))
        return
    
    start = 0
    if nums: start = randNums.index(nums[-1])
    for i in range(start, n):
        nums.append(randNums[i])
        solve(nums)
        nums.pop()

    return
solve([])