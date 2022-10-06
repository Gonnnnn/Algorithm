import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split(' '))
randNums = list(map(int, input().strip().split(' ')))
visited = [False for _ in range(n)]
randNums.sort()

def solve(nums):
    global n
    if len(nums) == m:
        print(' '.join(list(map(str, nums))))
        return
    temp = 0
    for i in range(n):
        if visited[i] or temp == randNums[i]: continue
        temp = randNums[i]
        nums.append(randNums[i])
        visited[i] = True
        solve(nums)
        visited[i] = False
        nums.pop()
    return
solve([])